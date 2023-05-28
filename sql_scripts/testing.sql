USE `bd2-23L-z09`;


-- pozyczka_na_karte_before_insert_trig
INSERT INTO POZYCZKI VALUES (NULL, 1200, 700, '2021-04-04', '2025-05-05', 25.55, 1, 'PLN', 2);
-- nie przechodzi, próba wzięcia pożyczki na kartę debetową


-- pozyczka_na_karte_before_update_trig
UPDATE POZYCZKI SET ID_karty = 2 WHERE ID_pozyczki = 2;
-- nie przechodzi, próba zaktualizowania pożyczki na kartę debetową


-- Zapytanie demonstruje działanie funkcji policz_calkowite_saldo.
-- Pokazuje ilość pieniędzy na wszystkich kontach, pożyczkach i lokatach każdego z klientów.
SELECT ID_klienta, 'konto' as typ, skrot_nazwy_waluty AS waluta, obecne_saldo,
       policz_calkowite_saldo(ID_klienta) as calkowite_saldo
FROM KLIENCI
INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
INNER JOIN KONTA USING(ID_konta)
INNER JOIN SALDA USING(ID_konta)
UNION
SELECT ID_klienta, 'pożyczka' as typ, skrot_nazwy_waluty AS waluta, -do_splaty AS balans,
       policz_calkowite_saldo(ID_klienta) as calkowite_saldo
FROM KLIENCI
INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
INNER JOIN KONTA USING(ID_konta)
INNER JOIN SALDA USING(ID_konta)
INNER JOIN POZYCZKI USING(ID_konta, skrot_nazwy_waluty)
UNION
SELECT ID_klienta, 'lokata' as typ, skrot_nazwy_waluty AS waluta, obecna_kwota AS balans,
       policz_calkowite_saldo(ID_klienta) as calkowite_saldo
FROM KLIENCI
INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
INNER JOIN KONTA USING(ID_konta)
INNER JOIN SALDA USING(ID_konta)
INNER JOIN LOKATY USING(ID_konta, skrot_nazwy_waluty);
