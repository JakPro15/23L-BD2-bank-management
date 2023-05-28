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
END;
