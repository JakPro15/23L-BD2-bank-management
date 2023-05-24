from contextlib import contextmanager
from os.path import expanduser

import PySide6.QtSql as sql
import re

from datatypes import AddressData, ClientData, PersonData, CompanyData
from database_errors import DatabaseConnectionError, DatabaseTransactionError, NoneValueError

class Database:
    def __init__(self) -> None:
        self.connection = sql.QSqlDatabase.addDatabase("QMYSQL")

        if not self.connection.isValid():
            error_text = self.connection.lastError().text()
            raise DatabaseConnectionError(
                f"Could not open a valid connection: {error_text}"
            )

        with open("others/connection_properties", "r") as file:
            user = file.readline().strip()
            password = file.readline().strip()
            port_nr = int(file.readline().strip())
            socket_path = file.readline().strip()

        self.connection.setConnectOptions(
            f"UNIX_SOCKET={expanduser(f'~/{socket_path}')}"
        )

        self.connection.setDatabaseName(user)
        self.connection.setPort(port_nr)
        self.connection.open(user, password)

        if self.connection.isOpenError():
            error_text = self.connection.lastError().text()
            raise DatabaseConnectionError(
                f"Could not connect to the database: {error_text}"
            )

    @contextmanager
    def transaction(self):
        self.connection.transaction()
        try:
            yield
            self.connection.commit()
        except DatabaseTransactionError:
            self.connection.rollback()
            raise

    @staticmethod
    def apartment_keyword(address_data: AddressData) -> str:
        if address_data.apartment_nr is None:
            return "IS"
        else:
            return "="
        
    def create_query(self, to_bind: object, query_str: str) -> sql.QSqlQuery:
        values_bound: list[str] = re.findall(r":[\w\d]+\b", query_str)

        query = sql.QSqlQuery(self.connection)
        query.prepare(query_str)

        for attribute_name in values_bound:
            query.bindValue(attribute_name, getattr(to_bind, attribute_name[1:], None))

        return query

    def check_address(self, address_data: AddressData) -> int | None:
        query_keyword: str = Database.apartment_keyword(address_data)

        query = self.create_query(address_data,
            "SELECT ID_adresu from ADRESY "
            "WHERE kraj = :country AND "
            "miejscowosc = :city AND "
            "kod_pocztowy = :post_code AND "
            "ulica = :street AND "
            "numer_domu = :house_nr AND "
            f"numer_mieszkania {query_keyword} :apartment_nr"
        )

        address_id: int | None = None

        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect specified address data"
            )
        
        if query.next():
            address_id = query.value(0)

        return address_id

    def add_client(self, client: ClientData) -> None:
        if client.address is None:
            raise NoneValueError

        with self.transaction():
            address_id: int | None = self.check_address(client.address)

            if address_id is None:
                address_query = self.create_query(client.address,
                    "INSERT INTO ADRESY (ID_adresu, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania) "
                    "VALUES (NULL, :country, :city, :post_code, :street, :house_nr, :apartment_nr)"
                )

                if not address_query.exec():
                    raise DatabaseTransactionError(
                        "Could not insert the address into the database"
                    )
                    
                address_id = self.check_address(client.address)

            client.address.address_id = address_id

            query = self.create_query(client,
                "INSERT INTO KLIENCI (ID_klienta, ID_adresu, email, numer_telefonu, selektor, imie, nazwisko, PESEL, plec, nazwa, NIP) "
                "VALUES (NULL, :address_id, :email, :nr_tel, :selector, :first_name, :last_name, :PESEL, :sex, :name, :NIP)"
            )

            if not query.exec():
                raise DatabaseTransactionError(
                    "Could not insert the client into the database"
                )

    def show_client_data_people(self) -> list[PersonData]:
        query = sql.QSqlQuery(self.connection)
        query.prepare(
            "SELECT ID_klienta, ID_adresu, email, numer_telefonu, imie, nazwisko, PESEL, plec FROM KLIENCI "
            "WHERE selektor = 'osoba'"
        )

        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect specified client data"
            )

        result: list[PersonData] = []
        while query.next():
            address_id: int = query.value("ID_adresu")

            address_query = sql.QSqlQuery(self.connection)

            address_query.prepare(
                "SELECT ID_adresu, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania FROM ADRESY "
                f"WHERE ID_adresu = {address_id}"
            )

            if not address_query.exec():
                raise DatabaseTransactionError(
                    "Could not collect specified address data"
                )
            
            if address_query.next():
                address = AddressData.from_query(address_query)

                data = PersonData(
                    client_id=query.value("ID_klienta"),
                    address=address,
                    email=query.value("email"),
                    nr_tel=query.value("numer_telefonu"),
                    first_name=query.value("imie"),
                    last_name=query.value("nazwisko"),
                    PESEL=query.value("PESEL"),
                    sex=query.value("plec")
                )
                result.append(data)

        return result
    
    def show_client_data_companies(self) -> list[CompanyData]:
        query = sql.QSqlQuery(self.connection)
        query.prepare(
            "SELECT ID_klienta, ID_adresu, email, numer_telefonu, nazwa, NIP FROM KLIENCI "
            "WHERE selektor = 'firma'"
        )

        if not query.exec():
            raise DatabaseTransactionError(
                "Could not collect specified client data"
            )

        result: list[CompanyData] = []
        while query.next():
            address_id: int = query.value("ID_adresu")

            address_query = sql.QSqlQuery(self.connection)

            address_query.prepare(
                "SELECT ID_adresu, kraj, miejscowosc, kod_pocztowy, ulica, numer_domu, numer_mieszkania FROM ADRESY "
                f"WHERE ID_adresu = {address_id}"
            )

            if not address_query.exec():
                raise DatabaseTransactionError(
                    "Could not collect specified address data"
                )
            
            if address_query.next():
                address = AddressData.from_query(address_query)

                data = CompanyData(
                    client_id=query.value("ID_klienta"),
                    address=address,
                    email=query.value("email"),
                    nr_tel=query.value("numer_telefonu"),
                    name=query.value("nazwa"),
                    NIP=query.value("NIP")
                )
                result.append(data)

        return result

    def delete_client(self, id: int) -> None:
        with self.transaction():
            query = sql.QSqlQuery(self.connection)
            query.prepare("DELETE FROM KLIENCI WHERE ID_klienta = :id")

            query.bindValue(":id", id)

            if not query.exec():
                raise DatabaseTransactionError(
                    "Could not delete the client from the database"
                )


if __name__ == "__main__":
    db = Database()
