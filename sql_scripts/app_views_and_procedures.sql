USE `bd2-23L-z09`;

DROP VIEW IF EXISTS KLIENCI_OSOBY, KLIENCI_FIRMY, KONTA_Z_TYPEM;
DROP PROCEDURE IF EXISTS adres_insert;
DROP PROCEDURE IF EXISTS osoba_insert;
DROP PROCEDURE IF EXISTS osoba_update;
DROP PROCEDURE IF EXISTS firma_insert;
DROP PROCEDURE IF EXISTS firma_update;
DROP PROCEDURE IF EXISTS klient_delete;
DROP PROCEDURE IF EXISTS typ_konta_insert;
DROP PROCEDURE IF EXISTS konto_insert;
DROP PROCEDURE IF EXISTS konto_update;
DROP PROCEDURE IF EXISTS konto_delete;

CREATE VIEW KLIENCI_OSOBY AS
    SELECT ID_klienta, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania,
           email, numer_telefonu, imie, nazwisko, PESEL, plec
    FROM KLIENCI INNER JOIN ADRESY USING(ID_adresu)
    WHERE selektor = 'osoba';


CREATE VIEW KLIENCI_FIRMY AS
    SELECT ID_klienta, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania,
           email, numer_telefonu, nazwa, NIP
    FROM KLIENCI INNER JOIN ADRESY USING(ID_adresu)
    WHERE selektor = 'firma';


CREATE VIEW KONTA_Z_TYPEM AS
    SELECT ID_konta, numer_konta, data_utworzenia, data_zamkniecia,
           IFNULL(limit_transakcji, -1.0) as limit_transakcji, nazwa, wersja
    FROM KONTA INNER JOIN TYPY_KONTA USING(ID_typu_konta);


DELIMITER //

CREATE PROCEDURE adres_insert(
    OUT p_id_adresu INT,
    IN p_kraj VARCHAR(40),
    IN p_miejscowosc VARCHAR(100),
    IN p_kod_pocztowy VARCHAR(10),
    IN p_ulica VARCHAR(100),
    IN p_numer_domu VARCHAR(8),
    IN p_numer_mieszkania VARCHAR(8)
)
BEGIN
    DECLARE v_id_adresu INT;
    DECLARE CONTINUE HANDLER FOR NOT FOUND BEGIN END;

    SELECT ID_adresu
    INTO v_id_adresu
    FROM ADRESY
    WHERE kraj = p_kraj AND miejscowosc = p_miejscowosc AND kod_pocztowy = p_kod_pocztowy
        AND ulica = p_ulica AND numer_domu = p_numer_domu AND numer_mieszkania <=> p_numer_mieszkania;

    IF v_id_adresu IS NULL THEN
        INSERT INTO ADRESY VALUES (NULL, p_kraj, p_miejscowosc, p_kod_pocztowy,
                                   p_ulica, p_numer_domu, p_numer_mieszkania);
        SELECT LAST_INSERT_ID()
        INTO v_id_adresu;
    END IF;

    SELECT v_id_adresu
    INTO p_id_adresu;
END//


CREATE PROCEDURE osoba_insert(
    OUT p_id_klienta INT,
    IN p_kraj VARCHAR(40),
    IN p_miejscowosc VARCHAR(100),
    IN p_kod_pocztowy VARCHAR(10),
    IN p_ulica VARCHAR(100),
    IN p_numer_domu VARCHAR(8),
    IN p_numer_mieszkania VARCHAR(8),
    IN p_email VARCHAR(50),
    IN p_numer_telefonu CHAR(14),
    IN p_imie VARCHAR(50),
    IN p_nazwisko VARCHAR(50),
    IN p_PESEL CHAR(11),
    IN p_plec CHAR(1)
)
BEGIN
    DECLARE v_id_adresu INT;

    CALL adres_insert(v_id_adresu, p_kraj, p_miejscowosc, p_kod_pocztowy,
                      p_ulica, p_numer_domu, p_numer_mieszkania);

    INSERT INTO KLIENCI VALUES(NULL, v_id_adresu, p_email, p_numer_telefonu, 'osoba',
                               p_imie, p_nazwisko, p_PESEL, p_plec, NULL, NULL);

    SELECT LAST_INSERT_ID()
    INTO p_id_klienta;
END//


CREATE PROCEDURE osoba_update(
    IN p_id_klienta INT,
    IN p_kraj VARCHAR(40),
    IN p_miejscowosc VARCHAR(100),
    IN p_kod_pocztowy VARCHAR(10),
    IN p_ulica VARCHAR(100),
    IN p_numer_domu VARCHAR(8),
    IN p_numer_mieszkania VARCHAR(8),
    IN p_email VARCHAR(50),
    IN p_numer_telefonu CHAR(14),
    IN p_imie VARCHAR(50),
    IN p_nazwisko VARCHAR(50),
    IN p_PESEL CHAR(11),
    IN p_plec CHAR(1)
)
BEGIN
    DECLARE v_stare_id_adresu INT;
    DECLARE v_id_adresu INT;
    DECLARE CONTINUE HANDLER FOR 1451 BEGIN END;

    IF (SELECT selektor FROM KLIENCI WHERE ID_klienta = p_id_klienta) <> 'osoba' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nie można zmienić firmy w osobę.';
    END IF;

    SELECT ID_adresu
    INTO v_stare_id_adresu
    FROM KLIENCI
    WHERE ID_klienta = p_id_klienta;

    CALL adres_insert(v_id_adresu, p_kraj, p_miejscowosc, p_kod_pocztowy,
                      p_ulica, p_numer_domu, p_numer_mieszkania);

    UPDATE KLIENCI
    SET ID_adresu = v_id_adresu, email = p_email, numer_telefonu = p_numer_telefonu,
        imie = p_imie, nazwisko = p_nazwisko, PESEL = p_PESEL, plec = p_plec
    WHERE ID_klienta = p_id_klienta;

    DELETE FROM ADRESY
    WHERE ID_adresu = v_stare_id_adresu;
END//


CREATE PROCEDURE firma_insert(
    OUT p_id_klienta INT,
    IN p_kraj VARCHAR(40),
    IN p_miejscowosc VARCHAR(100),
    IN p_kod_pocztowy VARCHAR(10),
    IN p_ulica VARCHAR(100),
    IN p_numer_domu VARCHAR(8),
    IN p_numer_mieszkania VARCHAR(8),
    IN p_email VARCHAR(50),
    IN p_numer_telefonu CHAR(14),
    IN p_nazwa VARCHAR(50),
    IN p_NIP CHAR(12)
)
BEGIN
    DECLARE v_id_adresu INT;

    CALL adres_insert(v_id_adresu, p_kraj, p_miejscowosc, p_kod_pocztowy,
                      p_ulica, p_numer_domu, p_numer_mieszkania);

    INSERT INTO KLIENCI VALUES(NULL, v_id_adresu, p_email, p_numer_telefonu, 'firma',
                               NULL, NULL, NULL, NULL, p_nazwa, p_NIP);

    SELECT LAST_INSERT_ID()
    INTO p_id_klienta;
END//


CREATE PROCEDURE firma_update(
    IN p_id_klienta INT,
    IN p_kraj VARCHAR(40),
    IN p_miejscowosc VARCHAR(100),
    IN p_kod_pocztowy VARCHAR(10),
    IN p_ulica VARCHAR(100),
    IN p_numer_domu VARCHAR(8),
    IN p_numer_mieszkania VARCHAR(8),
    IN p_email VARCHAR(50),
    IN p_numer_telefonu CHAR(14),
    IN p_nazwa VARCHAR(50),
    IN p_NIP CHAR(12)
)
BEGIN
    DECLARE v_stare_id_adresu INT;
    DECLARE v_id_adresu INT;
    DECLARE CONTINUE HANDLER FOR 1451 BEGIN END;

    IF (SELECT selektor FROM KLIENCI WHERE ID_klienta = p_id_klienta) <> 'firma' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nie można zmienić osoby w firmę.';
    END IF;

    SELECT ID_adresu
    INTO v_stare_id_adresu
    FROM KLIENCI
    WHERE ID_klienta = p_id_klienta;

    CALL adres_insert(v_id_adresu, p_kraj, p_miejscowosc, p_kod_pocztowy,
                      p_ulica, p_numer_domu, p_numer_mieszkania);

    UPDATE KLIENCI
    SET ID_adresu = v_id_adresu, email = p_email, numer_telefonu = p_numer_telefonu,
        nazwa = p_nazwa, NIP = p_NIP
    WHERE ID_klienta = p_id_klienta;

    DELETE FROM ADRESY
    WHERE ID_adresu = v_stare_id_adresu;
END//


CREATE PROCEDURE klient_delete(IN p_id_klienta INT)
BEGIN
    DECLARE v_stare_id_adresu INT;
    DECLARE CONTINUE HANDLER FOR 1451 BEGIN END;

    SELECT ID_adresu
    INTO v_stare_id_adresu
    FROM KLIENCI
    WHERE ID_klienta = p_id_klienta;

    DELETE FROM KLIENCI
    WHERE ID_klienta = p_id_klienta;

    DELETE FROM ADRESY
    WHERE ID_adresu = v_stare_id_adresu;
END//


CREATE PROCEDURE typ_konta_insert(
    OUT p_id_typu_konta INT,
    IN p_nazwa VARCHAR(50),
    IN p_wersja INT
)
BEGIN
    DECLARE v_id_typu_konta INT;
    DECLARE CONTINUE HANDLER FOR NOT FOUND BEGIN END;

    SELECT ID_typu_konta
    INTO v_id_typu_konta
    FROM TYPY_KONTA
    WHERE nazwa = p_nazwa AND wersja = p_wersja;

    IF v_id_typu_konta IS NULL THEN
        INSERT INTO TYPY_KONTA VALUES (NULL, p_nazwa, p_wersja);
        SELECT LAST_INSERT_ID()
        INTO v_id_typu_konta;
    END IF;

    SELECT v_id_typu_konta
    INTO p_id_typu_konta;
END//


CREATE PROCEDURE konto_insert(
    OUT p_id_konta INT,
    IN p_numer_konta CHAR(26),
    IN p_data_utworzenia DATE,
    IN p_data_zamkniecia DATE,
    IN p_limit_transakcji DECIMAL(40, 20),
    IN p_nazwa_typu_konta VARCHAR(50),
    IN p_wersja_typu_konta INT
)
BEGIN
    DECLARE v_id_typu_konta INT;

    CALL typ_konta_insert(v_id_typu_konta, p_nazwa_typu_konta, p_wersja_typu_konta);

    INSERT INTO KONTA VALUES(NULL, p_numer_konta, p_data_utworzenia,
                             p_data_zamkniecia, p_limit_transakcji, v_id_typu_konta);

    SELECT LAST_INSERT_ID()
    INTO p_id_konta;
END//


CREATE PROCEDURE konto_update(
    IN p_id_konta INT,
    IN p_numer_konta CHAR(26),
    IN p_data_utworzenia DATE,
    IN p_data_zamkniecia DATE,
    IN p_limit_transakcji DECIMAL(40, 20),
    IN p_nazwa_typu_konta VARCHAR(50),
    IN p_wersja_typu_konta INT
)
BEGIN
    DECLARE v_stare_id_typu_konta INT;
    DECLARE v_id_typu_konta INT;
    DECLARE CONTINUE HANDLER FOR 1451 BEGIN END;

    SELECT ID_typu_konta
    INTO v_stare_id_typu_konta
    FROM KONTA
    WHERE ID_konta = p_id_konta;

    CALL typ_konta_insert(v_id_typu_konta, p_nazwa_typu_konta, p_wersja_typu_konta);

    UPDATE KONTA
    SET numer_konta = p_numer_konta, data_utworzenia = p_data_utworzenia, data_zamkniecia = p_data_zamkniecia,
        limit_transakcji = p_limit_transakcji, ID_typu_konta = v_id_typu_konta
    WHERE ID_konta = p_id_konta;

    DELETE FROM TYPY_KONTA
    WHERE ID_typu_konta = v_stare_id_typu_konta;
END//


CREATE PROCEDURE konto_delete(IN p_id_konta INT)
BEGIN
    DECLARE v_stare_id_typu_konta INT;
    DECLARE CONTINUE HANDLER FOR 1451 BEGIN END;

    SELECT ID_typu_konta
    INTO v_stare_id_typu_konta
    FROM KONTA
    WHERE ID_konta = p_id_konta;

    DELETE FROM KONTA
    WHERE ID_konta = p_id_konta;

    DELETE FROM TYPY_KONTA
    WHERE ID_typu_konta = v_stare_id_typu_konta;
END//
