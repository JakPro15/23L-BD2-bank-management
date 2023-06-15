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


-- Wyzwalacz weryfikuje, czy data wzięcia branej pożyczki jest między założeniem, a zamknięciem konta.
CREATE TRIGGER data_pozyczki_trig
BEFORE UPDATE ON POZYCZKI
FOR EACH ROW
BEGIN
    DECLARE v_data_utworzenia_konta DATE;
    DECLARE v_data_zamkniecia_konta DATE;

    SELECT data_utworzenia, data_zamkniecia
    INTO v_data_utworzenia_konta, v_data_zamkniecia_konta
    FROM KONTA
    INNER JOIN SALDA USING(ID_konta)
    WHERE ID_konta = NEW.ID_konta AND skrot_nazwy_waluty = NEW.skrot_nazwy_waluty;

    IF NEW.data_wziecia < v_data_utworzenia_konta OR NEW.data_wziecia > v_data_zamkniecia_konta
    THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'To konto nie istniało w momencie wzięcia pożyczki!';
    END IF;
END//


-- Wyzwalacz weryfikuje, czy daty wzięcia i zakończenia tworzonej lokaty są między założeniem, a zamknięciem konta.
CREATE TRIGGER data_lokaty_trig
BEFORE UPDATE ON LOKATY
FOR EACH ROW
BEGIN
    DECLARE v_data_utworzenia_konta DATE;
    DECLARE v_data_zamkniecia_konta DATE;

    SELECT data_utworzenia, data_zamkniecia
    INTO v_data_utworzenia_konta, v_data_zamkniecia_konta
    FROM KONTA
    INNER JOIN SALDA USING(ID_konta)
    WHERE ID_konta = NEW.ID_konta AND skrot_nazwy_waluty = NEW.skrot_nazwy_waluty;

    IF NEW.data_zalozenia < v_data_utworzenia_konta OR NEW.data_zalozenia > v_data_zamkniecia_konta OR
       NEW.data_zakonczenia < v_data_utworzenia_konta OR NEW.data_zakonczenia > v_data_zamkniecia_konta
    THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'To konto nie istniało w momencie stworzenia lub zakończenia lokaty!';
    END IF;
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


-- Procedura wykonująca przelew wewnętrzny
CREATE PROCEDURE wykonaj_przelew_wewnetrzny(
    IN p_ID_nadawcy INT,
    IN p_ID_odbiorcy INT,
    IN p_kwota_do_przelania DECIMAL(40, 20),
    IN p_skrot_nazwy_waluty CHAR(3),
    IN p_tytul VARCHAR(50),
    IN p_adres_odbiorcy VARCHAR(100)
)
BEGIN
    DECLARE v_saldo_nadawcy DECIMAL(40, 20);
    DECLARE v_saldo_odbiorcy DECIMAL(40, 20);

    DECLARE CONTINUE HANDLER FOR NOT FOUND
    BEGIN
        IF v_saldo_nadawcy IS NULL
        THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nadawca nie posiada salda w podanej walucie';
        END IF;
        
        IF v_saldo_odbiorcy IS NULL
        THEN
            INSERT INTO SALDA VALUES (
                p_ID_odbiorcy, p_skrot_nazwy_waluty, 0
            );
            SET v_saldo_odbiorcy = 0;
        END IF;
    END;

    SELECT obecne_saldo
    INTO v_saldo_nadawcy
    FROM SALDA
    WHERE ID_konta = p_ID_nadawcy AND skrot_nazwy_waluty = p_skrot_nazwy_waluty;

    SELECT obecne_saldo
    INTO v_saldo_odbiorcy
    FROM SALDA
    WHERE ID_konta = p_ID_odbiorcy AND skrot_nazwy_waluty = p_skrot_nazwy_waluty;

    IF v_saldo_nadawcy < p_kwota_do_przelania
    THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nadawcy nie stać na przelew';
    END IF;

    UPDATE SALDA
    SET obecne_saldo = v_saldo_nadawcy - p_kwota_do_przelania
    WHERE ID_konta = p_ID_nadawcy AND skrot_nazwy_waluty = p_skrot_nazwy_waluty;

    UPDATE SALDA
    SET obecne_saldo = v_saldo_odbiorcy + p_kwota_do_przelania
    WHERE ID_konta = p_ID_odbiorcy AND skrot_nazwy_waluty = p_skrot_nazwy_waluty;

    INSERT INTO TRANSAKCJE VALUES (
        NULL, p_kwota_do_przelania, p_kwota_do_przelania,
        (CURRENT_DATE), p_tytul, p_adres_odbiorcy,
        p_ID_nadawcy, p_skrot_nazwy_waluty,
        p_ID_odbiorcy, p_skrot_nazwy_waluty,
        NULL
    );
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


-- Funkcja oblicza miesięczną opłatę za karty płatnicze dla danego klienta.
CREATE FUNCTION policz_oplate_za_karty_platnicze(p_ID_klienta INT)
RETURNS DECIMAL
DETERMINISTIC
BEGIN
    DECLARE c_oplata_karty_debetowej DECIMAL(40, 20) DEFAULT 5;
    DECLARE c_oplata_karty_kredytowej DECIMAL(40, 20) DEFAULT 10;
    DECLARE v_liczba_kart_debetowych INT;
    DECLARE v_liczba_kart_kredytowych INT;

    SELECT COUNT(*)
    INTO v_liczba_kart_debetowych
    FROM KLIENCI
    LEFT JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
    LEFT JOIN KONTA USING(ID_konta)
    LEFT JOIN KARTY k USING(ID_konta)
    WHERE ID_klienta = p_ID_klienta AND k.typ_karty = 'debit' AND
          (k.data_wygasniecia > (CURRENT_DATE) OR k.data_wygasniecia IS NULL)
          AND k.zablokowana = 0;

    SELECT COUNT(*)
    INTO v_liczba_kart_kredytowych
    FROM KLIENCI
    LEFT JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
    LEFT JOIN KONTA USING(ID_konta)
    LEFT JOIN KARTY k USING(ID_konta)
    WHERE ID_klienta = p_ID_klienta AND k.typ_karty = 'credit' AND
          (k.data_wygasniecia > (CURRENT_DATE) OR k.data_wygasniecia IS NULL)
          AND k.zablokowana = 0;

    RETURN v_liczba_kart_debetowych * c_oplata_karty_debetowej
            + v_liczba_kart_kredytowych * c_oplata_karty_kredytowej;
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
