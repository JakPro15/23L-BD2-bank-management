USE `bd2-23L-z09`;

DROP TABLE IF EXISTS TRANSAKCJE;
DROP TABLE IF EXISTS KONTA_ZEWNETRZNE;
DROP TABLE IF EXISTS BANKI;
DROP TABLE IF EXISTS LOKATY;
DROP TABLE IF EXISTS POZYCZKI;
DROP TABLE IF EXISTS SALDA;
DROP TABLE IF EXISTS WALUTY;
DROP TABLE IF EXISTS KARTY;
DROP TABLE IF EXISTS PRZYNALEZNOSCI_KONT;
DROP TABLE IF EXISTS KONTA;
DROP TABLE IF EXISTS TYPY_KONTA;
DROP TABLE IF EXISTS KLIENCI;
DROP TABLE IF EXISTS ADRESY;

DROP PROCEDURE IF EXISTS wyciagnij_z_lokaty;
DROP PROCEDURE IF EXISTS zaloz_lokate;
DROP PROCEDURE IF EXISTS splac_pozyczke;
DROP PROCEDURE IF EXISTS wez_pozyczke;
DROP PROCEDURE IF EXISTS sprawdz_pozyczke_na_karte;
DROP PROCEDURE IF EXISTS wykonaj_przewalutowanie;
DROP PROCEDURE IF EXISTS wykonaj_przelew_wewnetrzny;
DROP PROCEDURE IF EXISTS wykonaj_przelew_zewnetrzny;

DROP FUNCTION IF EXISTS policz_najblizszy_termin_splaty;
DROP FUNCTION IF EXISTS policz_oplate_za_karty_platnicze;
DROP FUNCTION IF EXISTS policz_calkowite_saldo;
