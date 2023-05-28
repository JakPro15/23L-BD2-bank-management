USE `bd2-23L-z09`;
DELIMITER //

-- procedura sprawdza, czy pożyczka nie jest wzięta na kartę debetową
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

-- wyzwalacz weryfikuje, czy pożyczka nie jest wzięta na kartę debetową przed dodaniem rekordu
CREATE TRIGGER pozyczka_na_karte_before_insert_trig
BEFORE INSERT ON POZYCZKI
FOR EACH ROW
BEGIN
    CALL sprawdz_pozyczke_na_karte(NEW.ID_karty);
END//

-- wyzwalacz weryfikuje, czy pożyczka nie jest wzięta na kartę debetową przed zaktualizowaniem rekordu
CREATE TRIGGER pozyczka_na_karte_before_update_trig
BEFORE UPDATE ON POZYCZKI
FOR EACH ROW
BEGIN
    CALL sprawdz_pozyczke_na_karte(NEW.ID_karty);
END//