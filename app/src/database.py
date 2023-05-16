import PySide6.QtSql as sql

from os.path import expanduser

class Database:
    def __init__(self) -> None:
        self.connection = sql.QSqlDatabase.addDatabase("QMYSQL")

        if(not self.connection.isValid()):
            raise ConnectionError(f"Could not open a valid connection: {self.connection.lastError().text()}")
        
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
            raise ConnectionError(f"Could not connect to the database: {self.connection.lastError().text()}")

    def select(self, column: str, table: str):
        result = []
        query = self.connection.exec(query=f'select {column} from {table}')

        while(query.next()):
            result.append(str(query.value(0)))

        return "\n".join(result)


if __name__ == "__main__":
    db = Database()
    print(db.select("nr", "bruh"))
