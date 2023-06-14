from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from src.database.abstract_data import Data, ModifiableData


@dataclass
class AddressData(Data):
    @staticmethod
    def table_name() -> str:
        return "ADRESY"

    @staticmethod
    def insert_procedure_name() -> str:
        return "adres_insert"

    @staticmethod
    def delete_procedure_name() -> str:
        return "adres_delete"

    country: str | None = None
    city: str | None = None
    post_code: str | None = None
    street: str | None = None
    house_nr: str | None = None
    apartment_nr: str | None = None


@dataclass
class ClientData(ModifiableData, ABC):
    client_id: int | None = None
    address: AddressData | None = None
    email: str | None = None
    phone_nr: str | None = None


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

    first_name: str | None = None
    last_name: str | None = None
    PESEL: str | None = None
    sex: str | None = None


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

    name: str | None = None
    NIP: str | None = None
