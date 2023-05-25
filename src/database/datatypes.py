import PySide6.QtSql as sql

from abc import ABC
from dataclasses import dataclass
from typing import Type

class Data(ABC):
    pass

@dataclass
class AddressData(Data):
    address_id: int | None = None
    country: str | None = None
    city: str | None = None
    post_code: str | None = None
    street: str | None = None
    house_nr: str | None = None
    apartment_nr: str | None = None

    @classmethod
    def from_query(cls, query: sql.QSqlQuery):
        return cls(
            address_id=query.value("ID_adresu"),
            country=query.value("kraj"),
            city=query.value("miejscowosc"),
            post_code=query.value("kod_pocztowy"),
            street=query.value("ulica"),
            house_nr=query.value("numer_domu"),
            apartment_nr=query.value("numer_mieszkania")
        )

@dataclass
class ClientData(Data, ABC):
    client_id: int | None = None
    address: AddressData | None = None
    email: str | None = None
    nr_tel: str | None = None

    @property
    def address_id(self) -> int | None:
        if self.address is not None:
            return self.address.address_id
        
    @property
    def selector(self) -> str:
        return ""
        

@dataclass
class PersonData(ClientData):
    first_name: str | None = None
    last_name: str | None = None
    PESEL: str | None = None
    sex: str | None = None

    @property
    def selector(self) -> str:
        return "osoba"
    
@dataclass
class CompanyData(ClientData):
    name: str | None = None
    NIP: str | None = None
    
    @property
    def selector(self) -> str:
        return "firma"

name_mapping: dict[Type[Data] | str, str] = {
    AddressData: "ADRESY",
    PersonData: "KLIENCI",
    CompanyData: "KLIENCI",
    "email": "email",
    "nr_tel": "numer_telefonu",
    "first_name": "imie",
    "last_name": "nazwisko",
    "PESEL": "PESEL",
    "sex": "plec",
    "name": "nazwa",
    "NIP": "NIP"
}