from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

import PySide6.QtSql as sql
from PySide6.QtCore import QDate

from src.database.abstract_data import Data, ModifiableData
from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError


@dataclass
class AddressData(Data):
    @staticmethod
    def table_name() -> str:
        return "ADRESY"

    country: str = None
    city: str = None
    post_code: str = None
    street: str = None
    house_nr: str = None
    apartment_nr: str | None = None

    def __str__(self) -> str:
        apartment_string = (
            f"/{self.apartment_nr}" if self.apartment_nr is not None else ""
        )
        return f"{self.street} {self.house_nr}{apartment_string}, {self.post_code} {self.city}, {self.country}"


@dataclass
class ClientData(ModifiableData, ABC):
    client_id: int | None = None
    address: AddressData = None
    email: str = None
    phone_nr: str = None

    def accounts(self, database) -> list[AccountData]:
        query = sql.QSqlQuery(database.connection)
        query.prepare(
            "SELECT * FROM KONTA_KLIENTOW WHERE ID_klienta = :client_id"
        )
        query.bindValue(":client_id", self.id)
        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect data from table KONTA_KLIENTOW"
            )
        result: list[AccountData] = []
        while query.next():
            data = AccountData.from_query(query)
            result.append(data)
        return result


@dataclass
class PersonData(ClientData):
    @staticmethod
    def table_name() -> str:
        return "KLIENCI_OSOBY"

    @staticmethod
    def insert_procedure_name() -> str:
        return "osoba_insert"

    @staticmethod
    def update_procedure_name() -> str:
        return "osoba_update"

    @staticmethod
    def delete_procedure_name() -> str:
        return "klient_delete"

    first_name: str = None
    last_name: str = None
    PESEL: str = None
    sex: str = None


@dataclass
class CompanyData(ClientData):
    @staticmethod
    def table_name() -> str:
        return "KLIENCI_FIRMY"

    @staticmethod
    def insert_procedure_name() -> str:
        return "firma_insert"

    @staticmethod
    def update_procedure_name() -> str:
        return "firma_update"

    @staticmethod
    def delete_procedure_name() -> str:
        return "klient_delete"

    name: str = None
    NIP: str = None


@dataclass
class AccountTypeData(Data):
    @staticmethod
    def table_name() -> str:
        return "TYPY_KONTA"

    @staticmethod
    def insert_procedure_name() -> str:
        return "typ_konta_insert"

    @staticmethod
    def delete_procedure_name() -> str:
        return "typ_konta_delete"

    name: str = None
    version: int = None

    def __str__(self) -> str:
        return f"{self.name} v.{self.version}"


@dataclass
class AccountData(ModifiableData):
    @staticmethod
    def table_name() -> str:
        return "KONTA_Z_TYPEM"

    @staticmethod
    def insert_procedure_name() -> str:
        return "konto_insert"

    @staticmethod
    def update_procedure_name() -> str:
        return "konto_update"

    @staticmethod
    def delete_procedure_name() -> str:
        return "konto_delete"

    account_id: int | None = None
    account_nr: str = None
    creation_date: QDate = None
    closing_date: QDate | None = None
    transaction_limit: float | None = None
    account_type: AccountTypeData = None

    def clients(self, database: Database) -> list[ClientData]:
        query = sql.QSqlQuery(database.connection)
        query.prepare(
            "SELECT * FROM WLASCICIELE_KONT WHERE ID_konta = :account_id"
        )
        query.bindValue(":account_id", self.id)
        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect data from table WLASCICIELE_KONT"
            )
        result: list[ClientData] = []
        while query.next():
            if query.value("selektor") == "osoba":
                result.append(PersonData.from_query(query))
            else:
                result.append(CompanyData.from_query(query))
        return result
    
@dataclass
class BankData(Data):
    @staticmethod
    def table_name() -> str:
        return "BANKI"

    bank_id: int = None
    name: str = None
    NIP: str = None
    address: AddressData = None

@dataclass
class OutsideAccountData(Data):
    @staticmethod
    def table_name() -> str:
        return "KONTA_ZEWNETRZNE"

    outside_account_id: int = None
    account_nr: str = None
    bank: BankData = None

@dataclass
class TransactionData(Data, ABC):
    transaction_id: int = None
    sum_before: float = None
    sum_after: float = None
    transaction_date: QDate = None
    title: str = None
    receiver_adress: str | None = None
    account_1_id: int = None
    short_currency_1: str = None

    def account_from(self, database: Database) -> AccountData:
        query = sql.QSqlQuery(database.connection)
        query.prepare(
            "SELECT * FROM SALDA_KONTA_WEWNETRZNE WHERE "
            "ID_konta = :account_1_id AND skrot_nazwy_waluty = :short_currency_1"
            )
        query.bindValue(":account_1_id", self.account_1_id)
        query.bindValue(":short_currency_1", self.short_currency_1)
        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect data from table SALDA_KONTA_WEWNETRZNE"
            )
        if query.next():
            result = AccountData.from_query(query)
        return result

@dataclass
class TransactionInsideData(TransactionData):
    @staticmethod
    def table_name() -> str:
        return "TRANSAKCJE_WEWNETRZNE"

    account_2_id: int = None
    short_currency_2: str = None
    
    def account_to(self, database: Database) -> AccountData:
        query = sql.QSqlQuery(database.connection)
        query.prepare(
            "SELECT * FROM SALDA_KONTA_WEWNETRZNE WHERE "
            "ID_konta = :account_2_id AND skrot_nazwy_waluty = :short_currency_2"
            )
        query.bindValue(":account_2_id", self.account_2_id)
        query.bindValue(":short_currency_2", self.short_currency_2)
        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect data from table SALDA_KONTA_WEWNETRZNE"
            )
        if query.next():
            result = AccountData.from_query(query)
        return result


@dataclass
class TransactionOutsideData(TransactionData):
    @staticmethod
    def table_name() -> str:
        return "TRANSAKCJE_ZEWNETRZNE"
    
    outside_account_id: int = None

    def account_to(self, database: Database) -> OutsideAccountData:
        query = sql.QSqlQuery(database.connection)
        query.prepare(
            "SELECT * FROM SALDA_KONTA_ZEWNETRZNE WHERE "
            "ID_konta_zewnetrznego = :outside_account_id"
            )
        query.bindValue(":outside_account_id", self.outside_account_id)
        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect data from table SALDA_KONTA_ZEWNETRZNE"
            )
        if query.next():
            result = OutsideAccountData.from_query(query)
        return result
