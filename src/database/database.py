from __future__ import annotations

from contextlib import contextmanager
from os.path import expanduser

import PySide6.QtSql as sql

from src.database.database_errors import (
    DatabaseConnectionError,
    DatabaseTransactionError
)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.database.abstract_data import Data


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

    def create_query(self, to_bind: Data, query_str: str) -> sql.QSqlQuery:
        query = sql.QSqlQuery(self.connection)
        query.prepare(query_str)
        to_bind.bind_non_id_attributes(query)
        return query

    def get_last_id(self) -> int:
        query = sql.QSqlQuery(self.connection)
        query.prepare("SELECT @id")

        if not query.exec():
            raise DatabaseTransactionError("Failed to read ID of last inserted object")

        query.next()
        return query.value("@id")


if __name__ == "__main__":
    db = Database()
