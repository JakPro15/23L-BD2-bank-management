USE `bd2-23L-z09`;

-- pozyczka_na_karte_before_insert_trig
INSERT INTO POZYCZKI VALUES (NULL, 1200, 700, '2021-04-04', '2025-05-05', 25.55, 1, 'PLN', 2);
-- nie przechodzi, próba wzięcia pożyczki na kartę debetową

-- pozyczka_na_karte_before_update_trig
UPDATE POZYCZKI SET ID_karty = 2 WHERE ID_pozyczki = 2;
-- nie przechodzi, próba zaktualizowania pożyczki na kartę debetową
