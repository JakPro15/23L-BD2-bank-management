import PySide6.QtSql as sql
from database_errors import DatabaseConnectionError, DatabaseTransactionError
from contextlib import contextmanager
from os.path import expanduser

class Database:
    def __init__(self) -> None:
        self.connection = sql.QSqlDatabase.addDatabase("QMYSQL")

        if(not self.connection.isValid()):
            raise DatabaseConnectionError(f"Could not open a valid connection: {self.connection.lastError().text()}")
        
        with open("others/connection_properties", "r") as file:
            user = file.readline().strip()
            password = file.readline().strip()
            port_nr = int(file.readline().strip())
            socket_path = file.readline().strip()

        self.connection.setConnectOptions(f"UNIX_SOCKET={expanduser(f'~/{socket_path}')}")

        self.connection.setDatabaseName(user)
        self.connection.setPort(port_nr)
        self.connection.open(user, password)

        if(self.connection.isOpenError()):
            raise DatabaseConnectionError(f"Could not connect to the database: {self.connection.lastError().text()}")

    @contextmanager
    def transaction(self):
        self.connection.transaction()
        try:
            yield
            self.connection.commit()
        except DatabaseTransactionError:
            self.connection.rollback()
            raise

    def add_client_person(self, adress: str, email: str, nr_tel: str, name: str, surname: str, PESEL: str, gender: str) -> None:
        with self.transaction():
            query = sql.QSqlQuery(self.connection)
            query.prepare(
                "INSERT INTO KLIENCI (ID_klienta, adres, email, numer_telefonu, selektor, imie, nazwisko, PESEL, plec) "
                "VALUES (NULL, :adress, :email, :nr_tel, 'osoba', :name, :surname, :PESEL, :gender)"
            )

            query.bindValue(":adress", adress)
            query.bindValue(":email", email)
            query.bindValue(":nr_tel", nr_tel)
            query.bindValue(":name", name)
            query.bindValue(":surname", surname)
            query.bindValue(":PESEL", PESEL)
            query.bindValue(":gender", gender)

            if not query.exec():
                raise DatabaseTransactionError(f"Could not insert the client into the database")
            
    def add_client_company(self, adress: str, email: str, nr_tel: str, name: str, NIP: str) -> None:
        with self.transaction():
            query = sql.QSqlQuery(self.connection)
            query.prepare(
                "INSERT INTO KLIENCI (ID_klienta, adres, email, numer_telefonu, selektor, nazwa, NIP) "
                "VALUES (NULL, :adres, :email, :nr_tel, 'firma', :name, :NIP)"
            )

            query.bindValue(":adress", adress)
            query.bindValue(":email", email)
            query.bindValue(":nr_tel", nr_tel)
            query.bindValue(":name", name)
            query.bindValue(":NIP", NIP)

            if not query.exec():
                raise DatabaseTransactionError(f"Could not insert the client into the database")
            
    def show_client_data_people(self) -> list[dict[str, int | str]]:
        query = sql.QSqlQuery(self.connection)
        query.prepare(
            "SELECT ID_klienta, adres, email, numer_telefonu, imie, nazwisko, PESEL, plec FROM KLIENCI "
            "WHERE selektor = 'osoba'"
        )

        if not query.exec():
            raise DatabaseTransactionError(f"Could not collect specified client data")
        
        result: list[dict[str, int | str]] = []
        while query.next():
            data = {
                "ID_klienta": query.value(0),
                "adres": query.value(1),
                "email": query.value(2),
                "numer_telefonu": query.value(3),
                "imie": query.value(4),
                "nazwisko": query.value(5),
                "PESEL": query.value(6),
                "plec": query.value(7),
            }
            result.append(data)

        return result
    
    def show_client_data_companies(self) -> list[dict[str, int | str]]:
        query = sql.QSqlQuery(self.connection)
        query.prepare(
            "SELECT ID_klienta, adres, email, numer_telefonu, nazwa, NIP FROM KLIENCI "
            "WHERE selektor = 'firma'"
        )

        if not query.exec():
            raise DatabaseTransactionError(f"Could not collect specified client data")
        
        result: list[dict[str, int | str]] = []
        while query.next():
            data = {
                "ID_klienta": query.value(0),
                "adres": query.value(1),
                "email": query.value(2),
                "numer_telefonu": query.value(3),
                "nazwa": query.value(4),
                "NIP": query.value(5)
            }
            result.append(data)

        return result
    
    def delete_client(self, id: int) -> None:
        with self.transaction():
            query = sql.QSqlQuery(self.connection)
            query.prepare("DELETE FROM KLIENCI WHERE ID_klienta = :id")

            query.bindValue(":id", id)

            if not query.exec():
                raise DatabaseTransactionError(f"Could not delete the client from the database")

if __name__ == "__main__":
    db = Database()
