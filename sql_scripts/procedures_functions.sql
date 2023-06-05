USE `bd2-23L-z09`;
DELIMITER //


-- Procedura sprawdza, czy pożyczka nie jest wzięta na kartę debetową
CREATE PROCEDURE sprawdz_pozyczke_na_karte(IN p_ID_karty INT)
BEGIN
    DECLARE v_typ_karty VARCHAR(6);

    IF p_ID_karty IS NOT NULL THEN
        SELECT typ_karty
        INTO v_typ_karty
        FROM KARTY
        WHERE ID_karty = p_ID_karty;

        IF v_typ_karty = 'debit' THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nie można wziąć pożyczki na kartę debetową.';
        END IF;
    END IF;
END//


-- Wyzwalacz weryfikuje, czy pożyczka nie jest wzięta na kartę debetową przed dodaniem rekordu
CREATE TRIGGER pozyczka_na_karte_before_insert_trig
BEFORE INSERT ON POZYCZKI
FOR EACH ROW
BEGIN
    CALL sprawdz_pozyczke_na_karte(NEW.ID_karty);
END//


-- Wyzwalacz weryfikuje, czy pożyczka nie jest wzięta na kartę debetową przed zaktualizowaniem rekordu
CREATE TRIGGER pozyczka_na_karte_before_update_trig
BEFORE UPDATE ON POZYCZKI
FOR EACH ROW
BEGIN
    CALL sprawdz_pozyczke_na_karte(NEW.ID_karty);
END//


-- Procedura rejestruje wzięcie pożyczki przez podane konto i dodaje pieniądze do konta.
CREATE PROCEDURE wez_pozyczke(IN p_poczatkowa_kwota DECIMAL(40,20), IN p_termin_splaty DATE,
                                      IN p_oprocentowanie DECIMAL(5,2), IN p_ID_konta INT,
                                      IN p_skrot_nazwy_waluty CHAR(3))
BEGIN
    DECLARE v_ID_konta INT;
    DECLARE v_skrot_nazwy_waluty CHAR(3);

    SELECT ID_konta, skrot_nazwy_waluty
    INTO v_ID_konta, v_skrot_nazwy_waluty
    FROM SALDA
    WHERE ID_konta = p_ID_konta AND skrot_nazwy_waluty = p_skrot_nazwy_waluty;

    UPDATE SALDA
    SET obecne_saldo = obecne_saldo + p_poczatkowa_kwota
    WHERE ID_konta = v_ID_konta AND skrot_nazwy_waluty = v_skrot_nazwy_waluty;

    INSERT INTO POZYCZKI VALUES (
        NULL, p_poczatkowa_kwota, p_poczatkowa_kwota, (CURRENT_DATE), p_termin_splaty,
        p_oprocentowanie, v_ID_konta, v_skrot_nazwy_waluty, NULL
    );

    -- TODO - obsługa sytuacji, w której chcemy wziąć pożyczkę na konto z niezarejestrowaną walutą
END//


-- Funkcja oblicza ogólne saldo w PLN wszystkich kont klienta, wliczając pożyczki i lokaty.
CREATE FUNCTION policz_calkowite_saldo(p_ID_klienta INT)
RETURNS DECIMAL
DETERMINISTIC
BEGIN
    DECLARE v_balans_calkowity DECIMAL(40, 20);
    DECLARE v_suma_lokat DECIMAL(40, 20);
    DECLARE v_suma_pozyczek DECIMAL(40, 20);

    SELECT SUM(s.obecne_saldo * w.kurs_wymiany_na_PLN)
    INTO v_balans_calkowity
    FROM SALDA s
    INNER JOIN WALUTY w USING(skrot_nazwy_waluty)
    INNER JOIN KONTA a USING(ID_konta)
    INNER JOIN PRZYNALEZNOSCI_KONT prk USING(ID_konta)
    WHERE prk.ID_klienta = p_ID_klienta;

    IF v_balans_calkowity IS NULL
    THEN
        SET v_balans_calkowity = 0;
    END IF;

    SELECT SUM(l.obecna_kwota * w.kurs_wymiany_na_PLN)
    INTO v_suma_lokat
    FROM LOKATY l
    INNER JOIN SALDA s USING(ID_konta, skrot_nazwy_waluty)
    INNER JOIN WALUTY w USING(skrot_nazwy_waluty)
    INNER JOIN KONTA k USING(ID_konta)
    INNER JOIN PRZYNALEZNOSCI_KONT prk USING(ID_konta)
    WHERE prk.ID_klienta = p_ID_klienta;

    IF v_suma_lokat IS NULL
    THEN
        SET v_suma_lokat = 0;
    END IF;

    SELECT SUM(p.do_splaty * w.kurs_wymiany_na_PLN)
    INTO v_suma_pozyczek
    FROM POZYCZKI p
    INNER JOIN SALDA s USING(ID_konta, skrot_nazwy_waluty)
    INNER JOIN WALUTY w USING(skrot_nazwy_waluty)
    INNER JOIN KONTA k USING(ID_konta)
    INNER JOIN PRZYNALEZNOSCI_KONT prk USING(ID_konta)
    WHERE prk.ID_klienta = p_ID_klienta;

    IF v_suma_pozyczek IS NULL
    THEN
        SET v_suma_pozyczek = 0;
    END IF;

    RETURN v_balans_calkowity + v_suma_lokat - v_suma_pozyczek;
END//
