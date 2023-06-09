from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Type, Self, Any, get_args, get_type_hints, TYPE_CHECKING
if TYPE_CHECKING:
    from .database import Database
from .database_errors import DatabaseTransactionError

import PySide6.QtSql as sql


class Data(ABC):
    @classmethod
    def from_query(cls, query: sql.QSqlQuery) -> Self:
        parameters: dict[str, Any] = {}
        for attribute in vars(cls()).keys():
            if attribute in attribute_mapping:
                parameters[attribute] = query.value(attribute_mapping[attribute])
            else:
                attribute_type: Type[Data] = get_args(get_type_hints(cls)[attribute])[0]
                parameters[attribute] = attribute_type.from_query(query)
        return cls(**parameters)  # type: ignore

    @classmethod
    def load_all(cls, database: Database) -> list[Self]:
        query = sql.QSqlQuery(database.connection)
        query.prepare(f"SELECT * FROM {view_mapping[cls]}")
        if not query.exec():
            raise DatabaseTransactionError(
                f"Could not collect data from table {view_mapping[cls]}"
            )
        result: list[Self] = []
        while query.next():
            data = cls.from_query(query)
            result.append(data)
        return result


@dataclass
class AddressData(Data):
    address_id: int | None = None
    country: str | None = None
    city: str | None = None
    post_code: str | None = None
    street: str | None = None
    house_nr: str | None = None
    apartment_nr: str | None = None


@dataclass
class ClientData(Data, ABC):
    client_id: int | None = None
    address: AddressData | None = None
    email: str | None = None
    phone_nr: str | None = None

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


view_mapping: dict[Type[Data], str] = {
    AddressData: "ADRESY",
    PersonData: "KLIENCI_OSOBY",
    CompanyData: "KLIENCI_FIRMY"
}


attribute_mapping: dict[str, str] = {
    "address_id": "ID_adresu",
    "country": "kraj",
    "city": "miejscowosc",
    "post_code": "kod_pocztowy",
    "street": "ulica",
    "house_nr": "numer_domu",
    "apartment_nr": "numer_mieszkania",
    "client_id": "ID_klienta",
    "email": "email",
    "phone_nr": "numer_telefonu",
    "first_name": "imie",
    "last_name": "nazwisko",
    "PESEL": "PESEL",
    "sex": "plec",
    "name": "nazwa",
    "NIP": "NIP",
}


if __name__ == "__main__":
    # inv_map = {v: k for k, v in name_mapping.items()}
    print(get_args(get_type_hints(ClientData)['address'])[0])
