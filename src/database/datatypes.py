from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Type, Self, Any, get_args, get_type_hints, TYPE_CHECKING
if TYPE_CHECKING:
    from .database import Database
from .database_errors import DatabaseTransactionError, IdMissingError

import PySide6.QtSql as sql


class Data(ABC):
    @staticmethod
    @abstractmethod
    def table_name() -> str:
        ...

    @staticmethod
    @abstractmethod
    def insert_procedure_name() -> str:
        ...

    @staticmethod
    @abstractmethod
    def delete_procedure_name() -> str:
        ...

    @classmethod
    def from_query(cls, query: sql.QSqlQuery) -> Self:
        parameters: dict[str, Any] = {}
        for attribute in vars(cls()):
            if attribute in attribute_mapping:
                parameters[attribute] = query.value(attribute_mapping[attribute])
            else:
                attribute_type: Type[Data] = get_args(get_type_hints(cls)[attribute])[0]
                parameters[attribute] = attribute_type.from_query(query)
        return cls(**parameters)  # type: ignore - Data.from_query won't be called anyway

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

    def _attribute_names_for_query(self) -> tuple[str, str]:
        attributes = ""
        id = ""
        first = True
        for attribute in vars(self):
            if attribute[-3:] == "_id":
                id = attribute
            else:
                if first:
                    first = False
                else:
                    attributes += ", "
                if attribute in attribute_mapping:
                    attributes += f":{attribute}"
                else:
                    attributes += getattr(self, attribute)._attribute_names_for_query()[1]
        return id, attributes

    @property
    def id(self) -> int:
        for attribute, value in vars(self).items():
            if attribute[-3:] == "_id":
                return value
        raise IdMissingError(f"Object of type {type(self).__name__} has no ID!")

    def bind_non_id_attributes(self, query: sql.QSqlQuery) -> None:
        for attribute in vars(self):
            if attribute in attribute_mapping:
                if f":{attribute}" in query.lastQuery():
                    query.bindValue(f":{attribute}", getattr(self, attribute))
            else:
                getattr(self, attribute).bind_non_id_attributes(query)

    def insert(self, database: Database) -> None:
        with database.transaction():
            id_name, attributes = self._attribute_names_for_query()
            query_string = f"CALL {self.insert_procedure_name()}(@id, {attributes})"
            query = database.create_query(self, query_string)
            print(query_string)
            if not query.exec():
                raise DatabaseTransactionError(
                    f"Could not insert a {type(self).__name__} object into the database, "
                    f"error: {query.lastError()}"
                )
        setattr(self, id_name, database.get_last_id())

    def delete(self, database: Database) -> None:
        with database.transaction():
            query_string = f"CALL {self.delete_procedure_name()}(:id)"
            query = database.create_query(self, query_string)
            query.bindValue(":id", self.id)
            if not query.exec():
                raise DatabaseTransactionError(
                    f"Could not delete a {type(self).__name__} object from the database, "
                    f"error: {query.lastError()}"
                )


class ModifiableData(Data, ABC):
    @staticmethod
    @abstractmethod
    def update_procedure_name() -> str:
        ...

    def update(self, database: Database):
        with database.transaction():
            id, attributes = self._attribute_names_for_query()
            query_string = f"CALL {self.update_procedure_name()}(:id, {attributes})"
            query = database.create_query(self, query_string)
            query.bindValue(":id", getattr(self, id))
            if not query.exec():
                raise DatabaseTransactionError(
                    f"Could not update a {type(self).__name__} object into the database, "
                    f"error: {query.lastError()}"
                )


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

    address_id: int | None = None
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
