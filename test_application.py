#!/usr/bin/python3.11

from src.database.database import Database
from src.database.datatypes import PersonData, CompanyData, AddressData


def test_osoby():
    database = Database()
    new = PersonData(None, AddressData(None, "Polska", "ABC", "11-400", "Waryńskiego", "5A", None),
                     "hehe@test.com", "123456789", "Ja", "Ty", "01232455644", "M")
    new.insert(database)
    assert new == PersonData.load_all(database)[-1]
