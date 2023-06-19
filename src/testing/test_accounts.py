#!/usr/bin/python3.11
from db_connection_testing import testing_database
from PySide6.QtCore import QDate

from src.database.table_types import AccountData, AccountTypeData


def test_account_insert(database):
    number_of_account_types = len(AccountTypeData.load_all(database))
    new1 = AccountData(
        None,
        "74125082031392539123895171",
        QDate(2023, 6, 14),
        None,
        None,
        AccountTypeData("oszcz", 1),
    )
    new1.insert(database)
    new2 = AccountData(
        None,
        "74125082031392123456867545",
        QDate(2022, 5, 14),
        QDate(2023, 2, 1),
        None,
        AccountTypeData("oszcz", 2),
    )
    new2.insert(database)
    assert new1 == AccountData.load_all(database)[-2]
    assert new2 == AccountData.load_all(database)[-1]
    assert (
        len(AccountTypeData.load_all(database)) == number_of_account_types + 2
    )


def test_account_update(database):
    number_of_account_types = len(AccountTypeData.load_all(database))
    updated = AccountData.load_all(database)[-2]
    updated.account_type.version = 2
    updated.creation_date = QDate(2010, 12, 24)
    updated.update(database)

    assert updated == AccountData.load_all(database)[-2]
    assert (
        len(AccountTypeData.load_all(database)) == number_of_account_types - 1
    )


def test_account_delete(database):
    deleted = AccountData.load_all(database)[-1]
    number_of_account_types = len(AccountTypeData.load_all(database))
    deleted.delete(database)
    assert deleted != AccountData.load_all(database)[-1]
    assert len(AccountTypeData.load_all(database)) == number_of_account_types
    deleted = AccountData.load_all(database)[-1]
    deleted.delete(database)
    assert deleted != AccountData.load_all(database)[-1]
    assert (
        len(AccountTypeData.load_all(database)) == number_of_account_types - 1
    )


def test_accounts_clients(database):
    account = AccountData.load_all(database)[1]
    owners = account.clients(database)
    assert {owner.id for owner in owners} == {2, 19}


if __name__ == "__main__":
    with testing_database() as database:
        test_account_insert(database)
        test_account_update(database)
        test_account_delete(database)
        test_accounts_clients(database)
