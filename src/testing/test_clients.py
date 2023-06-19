#!/usr/bin/python3.11
from db_connection_testing import testing_database

from src.database.table_types import AddressData, CompanyData, PersonData


def test_osoba_insert(database):
    number_of_addresses = len(AddressData.load_all(database))
    new1 = PersonData(
        None,
        AddressData("Polska", "ABC", "11-400", "Waryńskiego", "5A", None),
        "hehe@test.com",
        "123456789",
        "Ja",
        "Ty",
        "01232455644",
        "M",
    )
    new1.insert(database)
    new2 = PersonData(
        None,
        AddressData("Polska", "ABC", "11-400", "Waryńskiego", "34F", None),
        "hehe@test.com",
        "123456789",
        "Ja",
        "Ty",
        "01232455655",
        "M",
    )
    new2.insert(database)
    assert new1 == PersonData.load_all(database)[-2]
    assert new2 == PersonData.load_all(database)[-1]
    assert len(AddressData.load_all(database)) == number_of_addresses + 2


def test_osoba_update(database):
    number_of_addresses = len(AddressData.load_all(database))
    updated = PersonData.load_all(database)[-2]
    updated.address.house_nr = "34F"
    updated.phone_nr = "+48123654789"
    updated.update(database)

    assert updated == PersonData.load_all(database)[-2]
    assert len(AddressData.load_all(database)) == number_of_addresses - 1


def test_osoba_delete(database):
    deleted = PersonData.load_all(database)[-1]
    number_of_addresses = len(AddressData.load_all(database))
    deleted.delete(database)
    assert deleted != PersonData.load_all(database)[-1]
    assert len(AddressData.load_all(database)) == number_of_addresses
    deleted = PersonData.load_all(database)[-1]
    deleted.delete(database)
    assert deleted != PersonData.load_all(database)[-1]
    assert len(AddressData.load_all(database)) == number_of_addresses - 1


def test_company_insert(database):
    number_of_addresses = len(AddressData.load_all(database))
    new1 = CompanyData(
        None,
        AddressData("Polska", "ABC", "11-400", "Waryńskiego", "5A", None),
        "hehe@test.com",
        "123456789",
        "Ja",
        "012324556445",
    )
    new1.insert(database)
    new2 = CompanyData(
        None,
        AddressData("Polska", "ABC", "11-400", "Waryńskiego", "34F", None),
        "hehe@test.com",
        "123456789",
        "My",
        "012324556556",
    )
    new2.insert(database)
    assert new1 == CompanyData.load_all(database)[-2]
    assert new2 == CompanyData.load_all(database)[-1]
    assert len(AddressData.load_all(database)) == number_of_addresses + 2


def test_company_update(database):
    number_of_addresses = len(AddressData.load_all(database))
    updated = CompanyData.load_all(database)[-2]
    updated.address.house_nr = "34F"
    updated.phone_nr = "+48123654789"
    updated.update(database)

    assert updated == CompanyData.load_all(database)[-2]
    assert len(AddressData.load_all(database)) == number_of_addresses - 1


def test_company_delete(database):
    deleted = CompanyData.load_all(database)[-1]
    number_of_addresses = len(AddressData.load_all(database))
    deleted.delete(database)
    assert deleted != CompanyData.load_all(database)[-1]
    assert len(AddressData.load_all(database)) == number_of_addresses

    deleted = CompanyData.load_all(database)[-1]
    deleted.delete(database)
    assert deleted != CompanyData.load_all(database)[-1]
    assert len(AddressData.load_all(database)) == number_of_addresses - 1


def test_clients_accounts(database):
    person = PersonData.load_all(database)[0]
    accounts = person.accounts(database)
    assert {account.id for account in accounts} == {1, 26, 27, 28}


if __name__ == "__main__":
    with testing_database() as database:
        test_osoba_insert(database)
        test_osoba_update(database)
        test_osoba_delete(database)
        test_company_insert(database)
        test_company_update(database)
        test_company_delete(database)
        test_clients_accounts(database)
