USE `bd2-23L-z09`;

DROP VIEW IF EXISTS KLIENCI_OSOBY, KLIENCI_FIRMY;
DROP PROCEDURE IF EXISTS adres_insert;
DROP PROCEDURE IF EXISTS adres_delete;
DROP PROCEDURE IF EXISTS osoba_insert;
DROP PROCEDURE IF EXISTS osoba_update;
DROP PROCEDURE IF EXISTS firma_insert;
DROP PROCEDURE IF EXISTS firma_update;
DROP PROCEDURE IF EXISTS klient_delete;

CREATE VIEW KLIENCI_OSOBY AS
    SELECT ID_klienta, ID_adresu, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania,
           email, numer_telefonu, imie, nazwisko, PESEL, plec
    FROM KLIENCI INNER JOIN ADRESY USING(ID_adresu)
    WHERE selektor = 'osoba';


CREATE VIEW KLIENCI_FIRMY AS
    SELECT ID_klienta, ID_adresu, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania,
           email, numer_telefonu, nazwa, NIP
    FROM KLIENCI INNER JOIN ADRESY USING(ID_adresu)
    WHERE selektor = 'firma';


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
    IN p_numer_telefonu CHAR(10),
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
    IN p_numer_telefonu CHAR(10),
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
    IN p_numer_telefonu CHAR(10),
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
    IN p_numer_telefonu CHAR(10),
    IN p_nazwa VARCHAR(50),
    IN p_NIP CHAR(12)
)
BEGIN
    DECLARE v_id_adresu INT;

    IF (SELECT selektor FROM KLIENCI WHERE ID_klienta = p_id_klienta) <> 'firma' THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nie można zmienić osoby w firmę.';
    END IF;

    CALL adres_insert(v_id_adresu, p_kraj, p_miejscowosc, p_kod_pocztowy,
                      p_ulica, p_numer_domu, p_numer_mieszkania);

    UPDATE KLIENCI
    SET ID_adresu = v_id_adresu, email = p_email, numer_telefonu = p_numer_telefonu,
        nazwa = p_nazwa, NIP = p_NIP
    WHERE ID_klienta = p_id_klienta;
END//


CREATE PROCEDURE klient_delete(IN p_id_klienta INT)
BEGIN
    DELETE FROM KLIENCI
    WHERE ID_klienta = p_id_klienta;
END//
