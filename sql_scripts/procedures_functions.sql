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
CREATE PROCEDURE wez_pozyczke(IN p_poczatkowa_kwota DECIMAL(40, 20), IN p_termin_splaty DATE,
                                        IN p_oprocentowanie DECIMAL(5, 2), IN p_ID_konta INT,
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
    -- TODO - obsłużyć wzięcie pożyczki na kartę kredytową
END//


-- Procedura rejestruje spłatę pożyczki przez podane konto i odejmuje pieniądze z konta.
CREATE PROCEDURE splac_pozyczke(IN p_kwota_splaty DECIMAL(40, 20), IN p_ID_pozyczki INT)
BEGIN
    DECLARE v_do_splaty DECIMAL(40, 20);
    DECLARE v_ID_konta INT;
    DECLARE v_skrot_nazwy_waluty CHAR(3);
    DECLARE v_obecne_saldo DECIMAL(40, 20);
    DECLARE v_kwota_splaty DECIMAL(40, 20);

    SELECT do_splaty, ID_konta, skrot_nazwy_waluty
    INTO v_do_splaty, v_ID_konta, v_skrot_nazwy_waluty
    FROM POZYCZKI
    WHERE ID_pozyczki = p_ID_pozyczki;

    IF v_do_splaty > 0
    THEN
        SELECT obecne_saldo
        INTO v_obecne_saldo
        FROM SALDA
        WHERE ID_konta = v_ID_konta AND skrot_nazwy_waluty = v_skrot_nazwy_waluty;

        IF p_kwota_splaty > v_obecne_saldo OR p_kwota_splaty > v_do_splaty
        THEN
            SET v_kwota_splaty = LEAST(v_obecne_saldo, v_do_splaty);
        ELSE
            SET v_kwota_splaty = p_kwota_splaty;
        END IF;

        UPDATE SALDA
        SET obecne_saldo = obecne_saldo - v_kwota_splaty
        WHERE ID_konta = v_ID_konta AND skrot_nazwy_waluty = v_skrot_nazwy_waluty;

        UPDATE POZYCZKI
        SET do_splaty = do_splaty - v_kwota_splaty
        WHERE ID_pozyczki = p_ID_pozyczki;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ta pożyczka została już opłacona!';
    END IF;
END//


-- Procedura rejestruje założenie lokaty przez podane konto i odejmuje pieniądze z konta.
CREATE PROCEDURE zaloz_lokate(IN p_kwota DECIMAL(40, 20), IN p_data_konca_blokady DATE,
                                    IN p_oprocentowanie DECIMAL(5, 2), IN p_ID_konta INT,
                                    IN p_skrot_nazwy_waluty CHAR(3))
BEGIN
    DECLARE v_ID_konta INT;
    DECLARE v_skrot_nazwy_waluty CHAR(3);
    DECLARE v_obecne_saldo DECIMAL(40, 20);

    SELECT ID_konta, skrot_nazwy_waluty, obecne_saldo
    INTO v_ID_konta, v_skrot_nazwy_waluty, v_obecne_saldo
    FROM SALDA
    WHERE ID_konta = p_ID_konta AND skrot_nazwy_waluty = p_skrot_nazwy_waluty;

    IF v_obecne_saldo >= p_kwota
    THEN
        UPDATE SALDA
        SET obecne_saldo = obecne_saldo - p_kwota
        WHERE ID_konta = v_ID_konta AND skrot_nazwy_waluty = v_skrot_nazwy_waluty;

        INSERT INTO LOKATY VALUES (
            NULL, p_kwota, (CURRENT_DATE), NULL, p_data_konca_blokady, p_oprocentowanie,
            v_ID_konta, v_skrot_nazwy_waluty
        );
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Tego konta nie stać na założenie takiej lokaty!';
    END IF;
END//


-- Procedura rejestruje wyjęcie pieniędzy z lokaty przez podane konto i dodaje pieniądze do konta.
CREATE PROCEDURE wyciagnij_z_lokaty(IN p_kwota_do_wyjecia DECIMAL(40, 20), IN p_ID_lokaty INT)
BEGIN
    DECLARE v_obecna_kwota DECIMAL(40, 20);
    DECLARE v_data_konca_blokady DATE;
    DECLARE v_ID_konta INT;
    DECLARE v_skrot_nazwy_waluty CHAR(3);
    DECLARE v_kwota_do_wyjecia DECIMAL(40, 20);

    SELECT obecna_kwota, data_konca_blokady, ID_konta, skrot_nazwy_waluty
    INTO v_obecna_kwota, v_data_konca_blokady, v_ID_konta, v_skrot_nazwy_waluty
    FROM LOKATY
    WHERE ID_lokaty = p_ID_lokaty;

    IF v_obecna_kwota > 0
    THEN
        IF v_data_konca_blokady IS NULL OR (CURRENT_DATE) >= v_data_konca_blokady
        THEN
            IF p_kwota_do_wyjecia > v_obecna_kwota
            THEN
                SET v_kwota_do_wyjecia = v_obecna_kwota;

                UPDATE LOKATY
                SET data_zakonczenia = (CURRENT_DATE), obecna_kwota = 0
                WHERE ID_lokaty = p_ID_lokaty;
            ELSE
                SET v_kwota_do_wyjecia = p_kwota_do_wyjecia;

                UPDATE LOKATY
                SET obecna_kwota = obecna_kwota - v_kwota_do_wyjecia
                WHERE ID_lokaty = p_ID_lokaty;
            END IF;

            UPDATE SALDA
            SET obecne_saldo = obecne_saldo + v_kwota_do_wyjecia
            WHERE ID_konta = v_ID_konta AND skrot_nazwy_waluty = v_skrot_nazwy_waluty;
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nie możesz wyjąć pieniędzy przed zakończeniem blokady!';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ta lokata jest już pusta!';
    END IF;
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


-- Funkcja oblicza termin spłaty najbliższej pożyczki wziętej przez klienta
CREATE FUNCTION policz_najblizszy_termin_splaty(p_ID_klienta INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE v_termin_splaty DATE;

    SELECT min(termin_splaty)
    INTO v_termin_splaty
    FROM POZYCZKI
    INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_konta)
    INNER JOIN KLIENCI USING(ID_klienta)
    WHERE ID_klienta = p_ID_klienta AND do_splaty > 0;

    IF v_termin_splaty IS NULL
    THEN
        RETURN -1;
    ELSEIF v_termin_splaty <= (CURRENT_DATE)
    THEN
        RETURN 0;
    ELSE
        RETURN DATEDIFF(v_termin_splaty, (CURRENT_DATE));
    END IF;
END//
