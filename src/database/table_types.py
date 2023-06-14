from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from PySide6.QtCore import QDate
import PySide6.QtSql as sql

from src.database.database import Database
from src.database.database_errors import DatabaseTransactionError
from src.database.abstract_data import Data, ModifiableData


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


@dataclass
class ClientData(ModifiableData, ABC):
    client_id: int | None = None
    address: AddressData = None
    email: str = None
    phone_nr: str = None

    def accounts(self, database) -> list[AccountData]:
        query = sql.QSqlQuery(database.connection)
        query.prepare("SELECT * FROM KONTA_KLIENTOW WHERE ID_klienta = :client_id")
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
        query.prepare("SELECT * FROM WLASCICIELE_KONT WHERE ID_konta = :account_id")
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
