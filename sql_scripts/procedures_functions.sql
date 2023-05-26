USE `bd2-23L-z09`;

-- wyzwalacz weryfikuje, czy pozyczka nie jest wzieta na karte debetowa
-- DROP TRIGGER pozyczka_na_karte_trig;
delimiter //

CREATE TRIGGER pozyczka_na_karte_trig
BEFORE INSERT ON POZYCZKI
FOR EACH ROW
BEGIN
    DECLARE v_typ_karty VARCHAR(6);

    IF NEW.ID_karty IS NOT NULL
    THEN
        SELECT typ_karty
        FROM KARTY
        WHERE ID_karty = NEW.ID_karty
        INTO v_typ_karty;

        IF v_typ_karty = 'debit'
        THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Nie mozna wziac pozyczki na karte debetowa.';
        END IF;
    END IF;
END//
