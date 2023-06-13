-- pozyczka_na_karte_before_insert_trig
INSERT INTO POZYCZKI VALUES (NULL, 1200, 700, '2021-04-04', '2025-05-05', 25.55, 1, 'PLN', 2);
-- nie przechodzi, próba wzięcia pożyczki na kartę debetową


-- pozyczka_na_karte_before_update_trig
UPDATE POZYCZKI SET ID_karty = 2 WHERE ID_pozyczki = 2;
-- nie przechodzi, próba zaktualizowania pożyczki na kartę debetową


-- data_pozyczki_trig
UPDATE POZYCZKI SET data_wziecia = '1955-01-01' WHERE ID_pozyczki = 1;
-- nie przechodzi, próba zaktualizowania daty wzięcia pożyczki na odległą datę


-- data_lokaty_trig
UPDATE LOKATY SET data_zalozenia = '1955-01-01' WHERE ID_lokaty = 1;
-- nie przechodzi, próba zaktualizowania daty założenia lokaty na odległą datę


-- Poniżej jest demonstracja działania procedury wez_pozyczke.
-- Stan konta sprzed wzięcia pożyczki:
SELECT ID_konta, skrot_nazwy_waluty, obecne_saldo
FROM SALDA
WHERE ID_konta = 10;

-- Bierzemy pożyczkę:
CALL wez_pozyczke(10000, '2025-04-06', 7 / 100, 10, 'PLN');

-- Ilość pieniędzy na koncie wzrosła.
SELECT ID_konta, skrot_nazwy_waluty, obecne_saldo
FROM SALDA
WHERE ID_konta = 10;

-- Pożyczka została też dodana do tabeli POZYCZKI.
SELECT *
FROM POZYCZKI
ORDER BY data_wziecia DESC
LIMIT 1;


-- Poniżej jest demonstracja działania procedury splac_pozyczke.
-- Stan konta i zadłużenie przed spłatą pożyczki:
SELECT s.ID_konta, s.skrot_nazwy_waluty, s.obecne_saldo, p.do_splaty
FROM SALDA s
INNER JOIN POZYCZKI p USING(ID_konta, skrot_nazwy_waluty)
WHERE p.ID_pozyczki = 3;

-- Spłacamy pożyczkę:
CALL splac_pozyczke(1400, 3);

-- Pożyczka została opłacona, a kwota została odjęta z salda:
SELECT s.ID_konta, s.skrot_nazwy_waluty, s.obecne_saldo, p.do_splaty
FROM SALDA s
INNER JOIN POZYCZKI p USING(ID_konta, skrot_nazwy_waluty)
WHERE p.ID_pozyczki = 3;


-- Poniżej jest demonstracja działania procedury zaloz_lokate.
-- Stan konta sprzed założenia lokaty:
SELECT ID_konta, skrot_nazwy_waluty, obecne_saldo
FROM SALDA
WHERE ID_konta = 10;

-- Zakładamy lokatę:
CALL zaloz_lokate(3000, '2025-05-05', 3 / 100, 10, 'PLN');

-- Tlość pieniędzy na koncie zmalała.
SELECT ID_konta, skrot_nazwy_waluty, obecne_saldo
FROM SALDA
WHERE ID_konta = 10;

-- Lokata została też dodana do tabeli LOKATY.
SELECT *
FROM LOKATY
ORDER BY data_zalozenia DESC
LIMIT 1;


-- Poniżej jest demonstracja działania procedury wyciagnij_z_lokaty.
-- Stan konta i kwota na lokacie przed wyjęciem środków:
SELECT s.ID_konta, s.skrot_nazwy_waluty, s.obecne_saldo, l.obecna_kwota, l.data_zakonczenia
FROM SALDA s
INNER JOIN LOKATY l USING(ID_konta, skrot_nazwy_waluty)
WHERE l.ID_lokaty = 1;

-- Wyciągamy wszystkie środki z lokaty (oczywiście moglibyśmy również i mniej):
CALL wyciagnij_z_lokaty(26700, 1);

-- Lokata pomniejszyła się, ustawiona została data zakończenia na dzisiejszą,
-- a kwota została dodana do salda:
SELECT s.ID_konta, s.skrot_nazwy_waluty, s.obecne_saldo, l.obecna_kwota, l.data_zakonczenia
FROM SALDA s
INNER JOIN LOKATY l USING(ID_konta, skrot_nazwy_waluty)
WHERE l.ID_lokaty = 1;

-- Nie możemy wyciągnąć środków z lokaty, na której blokada jeszcze nie minęła:
SELECT s.ID_konta, s.skrot_nazwy_waluty, s.obecne_saldo, l.obecna_kwota, l.data_konca_blokady
FROM SALDA s
INNER JOIN LOKATY l USING(ID_konta, skrot_nazwy_waluty)
WHERE l.ID_lokaty = 5;

-- Próba wyciągnięcia środków z lokaty:
CALL wyciagnij_z_lokaty(100, 5);
-- Kończy się niepowodzeniem i zasygnalizowaną informacją.


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


-- Zapytanie demonstruje działanie funkcji policz_oplate_za_karty_platnicze.
-- nie przechodzi
SELECT ID_klienta, policz_oplate_za_karty_platnicze(ID_klienta),
        NVL(karty_debetowe, 0) AS karty_debetowe,
        NVL(karty_kredytowe, 0) AS karty_kredytowe
FROM KLIENCI
LEFT JOIN (SELECT ID_klienta, COUNT(ID_karty) AS karty_debetowe
           FROM KLIENCI
           INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
           INNER JOIN KONTA USING(ID_konta)
           INNER JOIN KARTY USING(ID_konta)
           WHERE zablokowana = 0 AND ((CURRENT_DATE) < data_wygasniecia OR data_wygasniecia IS NULL) AND KARTY.typ_karty = 'debit'
           GROUP BY ID_klienta) USING(ID_klienta)
LEFT JOIN (SELECT ID_klienta, COUNT(ID_karty) AS karty_kredytowe
           FROM KLIENCI
           INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_klienta)
           INNER JOIN KONTA USING(ID_konta)
           INNER JOIN KARTY USING(ID_konta)
           WHERE zablokowana = 0 AND ((CURRENT_DATE) < data_wygasniecia OR data_wygasniecia IS NULL) AND KARTY.typ_karty = 'credit'
           GROUP BY ID_klienta) USING(ID_klienta)
ORDER BY ID_klienta;
-- druga wersja:
SELECT ID_klienta, policz_oplate_za_karty_platnicze(ID_klienta) AS "miesięczna opŁata za karty"
FROM KLIENCI;


-- Zapytanie demonstruje działanie funkcji policz_najblizszy_termin_splaty.
SELECT ID_klienta, min(termin_splaty) AS "koniec terminu najbliższej pożyczki",
        policz_najblizszy_termin_splaty(ID_klienta) AS "dni do spłaty"
FROM POZYCZKI
INNER JOIN PRZYNALEZNOSCI_KONT USING(ID_konta)
INNER JOIN KLIENCI USING(ID_klienta)
GROUP BY ID_klienta;
