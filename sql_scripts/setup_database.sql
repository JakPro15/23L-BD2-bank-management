USE `bd2-23L-z09`;

CREATE TABLE ADRESY (
    ID_adresu INT AUTO_INCREMENT PRIMARY KEY,
    kraj VARCHAR(40) NOT NULL,
    miejscowosc VARCHAR(100) NOT NULL,
    kod_pocztowy VARCHAR(10) NOT NULL,
    ulica VARCHAR(100) NOT NULL,
    numer_domu VARCHAR(8) NOT NULL,
    numer_mieszkania VARCHAR(8)
);

CREATE TABLE KLIENCI (
    ID_klienta INT AUTO_INCREMENT PRIMARY KEY,
    ID_adresu INT NOT NULL REFERENCES ADRESY(ID_adresu),
    email VARCHAR(50),
    numer_telefonu CHAR(10),
    selektor CHAR(5) NOT NULL,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    PESEL CHAR(11),
    plec CHAR(1),
    nazwa VARCHAR(50),
    NIP CHAR(12),
    CONSTRAINT kontakt CHECK(numer_telefonu IS NOT NULL OR email IS NOT NULL),
    CONSTRAINT podtyp CHECK(
        (selektor = 'osoba'
            AND imie IS NOT NULL AND nazwisko IS NOT NULL AND PESEL IS NOT NULL AND plec IS NOT NULL
            AND nazwa IS NULL AND NIP IS NULL)
        OR
        (selektor = 'firma'
            AND nazwa IS NOT NULL AND NIP IS NOT NULL
            AND imie IS NULL AND nazwisko IS NULL AND PESEL IS NULL AND plec IS NULL)
    )
);

CREATE TABLE TYPY_KONTA (
    ID_typu_konta INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(50) NOT NULL,
    wersja INT NOT NULL
);

CREATE TABLE KONTA (
    ID_konta INT AUTO_INCREMENT PRIMARY KEY,
    numer_konta CHAR(26) NOT NULL UNIQUE,
    data_utworzenia DATE NOT NULL DEFAULT (CURRENT_DATE),
    data_zakonczenia DATE,
    limit_transakcji DECIMAL(40, 20),
    ID_typu_konta INT NOT NULL REFERENCES TYPY_KONTA(ID_typu_konta),
    CONSTRAINT zamkniecie_po_otwarciu CHECK(data_zakonczenia IS NULL OR
                                        data_zakonczenia >= data_utworzenia)
);

CREATE TABLE PRZYNALEZNOSCI_KONT (
    ID_klienta INT NOT NULL,
    ID_konta INT NOT NULL,
    CONSTRAINT fk_przynaleznosci_kont_klienci FOREIGN KEY (ID_klienta) REFERENCES KLIENCI(ID_klienta),
    CONSTRAINT fk_przynaleznosci_kont_konta FOREIGN KEY (ID_konta) REFERENCES KONTA(ID_konta),
    PRIMARY KEY (ID_klienta, ID_konta)
);

CREATE TABLE KARTY (
    ID_karty INT AUTO_INCREMENT PRIMARY KEY,
    numer_karty CHAR(16) NOT NULL UNIQUE,
    limit_transakcji DECIMAL(40, 20) CHECK(limit_transakcji >= 0),
    data_wygasniecia DATE NOT NULL,
    zablokowana BOOLEAN DEFAULT 0 NOT NULL,
    typ_karty CHAR(6) NOT NULL,
    ID_konta INT NOT NULL REFERENCES KONTA(ID_konta)
);

CREATE TABLE WALUTY (
    skrot_nazwy_waluty CHAR(3) NOT NULL PRIMARY KEY,
    pelna_nazwa VARCHAR(50) NOT NULL,
    kurs_wymiany_na_PLN DECIMAL(40, 20) NOT NULL CHECK(kurs_wymiany_na_PLN > 0)
);

CREATE TABLE SALDA (
    ID_konta INT NOT NULL REFERENCES KONTA(ID_konta),
    skrot_nazwy_waluty CHAR(3) NOT NULL REFERENCES WALUTY(skrot_nazwy_waluty),
    obecne_saldo DECIMAL(40, 20) NOT NULL,
    CONSTRAINT salda_pk PRIMARY KEY (ID_konta, skrot_nazwy_waluty)
);

CREATE TABLE POZYCZKI (
    ID_pozyczki INT AUTO_INCREMENT PRIMARY KEY,
    poczatkowa_kwota DECIMAL(40, 20) NOT NULL CHECK(poczatkowa_kwota > 0),
    do_splaty DECIMAL(40, 20) NOT NULL CHECK(do_splaty >= 0),
    data_wziecia DATE DEFAULT (CURRENT_DATE) NOT NULL,
    termin_splaty DATE NOT NULL,
    oprocentowanie DECIMAL(5, 2) NOT NULL CHECK(oprocentowanie >= 0),
    ID_konta INT NOT NULL REFERENCES SALDA(ID_konta),
    skrot_nazwy_waluty CHAR(3) NOT NULL REFERENCES SALDA(skrot_nazwy_waluty),
    ID_karty INT REFERENCES KARTY(ID_karty),
    CONSTRAINT splata_po_wzieciu CHECK(termin_splaty >= data_wziecia)
);

CREATE TABLE LOKATY (
    ID_lokaty INT AUTO_INCREMENT PRIMARY KEY,
    obecna_kwota DECIMAL(40, 20) NOT NULL CHECK(obecna_kwota > 0),
    data_zalozenia DATE DEFAULT (CURRENT_DATE) NOT NULL,
    data_zakonczenia DATE,
    data_konca_blokady DATE,
    oprocentowanie DECIMAL(5, 2) NOT NULL CHECK(oprocentowanie >= 0),
    ID_konta INT NOT NULL REFERENCES SALDA(ID_konta),
    skrot_nazwy_waluty CHAR(3) NOT NULL REFERENCES SALDA(skrot_nazwy_waluty),
    CONSTRAINT kolejnosc_dat CHECK(data_konca_blokady >= data_zalozenia AND
                                   data_zakonczenia >= data_konca_blokady AND
                                   data_zakonczenia >= data_zalozenia)
);

CREATE TABLE BANKI (
    ID_banku INT AUTO_INCREMENT PRIMARY KEY,
    nazwa VARCHAR(50) NOT NULL,
    NIP CHAR(12) NOT NULL,
    ID_adresu INT NOT NULL REFERENCES ADRESY(ID_adresu)
);

CREATE TABLE KONTA_ZEWNETRZNE (
    ID_konta_zewnetrznego INT AUTO_INCREMENT PRIMARY KEY,
    numer_konta CHAR(26) NOT NULL UNIQUE,
    ID_banku INT NOT NULL REFERENCES BANKI(ID_banku)
);

CREATE TABLE TRANSAKCJE (
    ID_transakcji INT AUTO_INCREMENT PRIMARY KEY,
    kwota_przed DECIMAL(40, 20) NOT NULL,
    kwota_po DECIMAL(40, 20) NOT NULL,
    data_transakcji DATE DEFAULT (CURRENT_DATE) NOT NULL,
    tytul VARCHAR(50) NOT NULL,
    adres_odbiorcy VARCHAR(100),
    ID_konta_1 INT NOT NULL REFERENCES SALDA(ID_konta),
    skrot_nazwy_waluty_1 CHAR(3) NOT NULL REFERENCES SALDA(skrot_nazwy_waluty),
    ID_konta_2 INT REFERENCES SALDA(ID_konta),
    skrot_nazwy_waluty_2 CHAR(3) REFERENCES SALDA(skrot_nazwy_waluty),
    ID_konta_zewnetrznego INT REFERENCES KONTA_ZEWNETRZNE(ID_konta_zewnetrznego),
    CONSTRAINT luk CHECK(
        (ID_konta_2 IS NOT NULL AND skrot_nazwy_waluty_2 IS NOT NULL AND ID_konta_zewnetrznego IS NULL)
        OR
        (ID_konta_2 IS NULL AND skrot_nazwy_waluty_2 IS NULL AND ID_konta_zewnetrznego IS NOT NULL)
    )
);
