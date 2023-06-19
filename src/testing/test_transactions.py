#!/usr/bin/python3.11
from PySide6.QtCore import QDate
from db_connection_testing import testing_database
from src.database.table_types import (
    AccountData, AccountTypeData, OutsideAccountData,
    BankData, AddressData, TransactionInsideData, TransactionOutsideData
    )

def test_transakcje_wewnetrzne_load(database):
    transakcje = TransactionInsideData.load_all(database)
    first = transakcje[0]
    correct = TransactionInsideData(
        transaction_id=1, sum_before=230.0,
        sum_after=230.0, transaction_date=QDate(2020, 10, 13),
        title='Teleporter do podróży w czasie',
        receiver_adress=None, account_1_id=27,
        short_currency_1='PLN', account_2_id=15, short_currency_2='PLN')
    assert first == correct

def test_transakcje_zewnetrzne_load(database):
    transakcje = TransactionOutsideData.load_all(database)
    first = transakcje[0]
    correct = TransactionOutsideData(
        transaction_id=25, sum_before=-31900.0,
        sum_after=-31900.0, transaction_date=QDate(2020, 5, 4),
        title='Czynsz', receiver_adress=None, account_1_id=11,
        short_currency_1='PLN', outside_account_id=1)
    assert first == correct

def test_account_from(database):
    transakcje = TransactionInsideData.load_all(database)
    first = transakcje[0]
    account = first.account_from(database)
    correct = AccountData(
        account_id=27, account_nr='56125033825860600076653641',
        creation_date=QDate(2009, 7, 25), closing_date=None,
        transaction_limit=10000.0, account_type=AccountTypeData(name='firmowe', version=4))
    assert account == correct

def test_account_to_inside(database):
    transakcje = TransactionInsideData.load_all(database)
    first = transakcje[0]
    account = first.account_to(database)
    correct = AccountData(
        account_id=15, account_nr='89125070456398485226675850', 
        creation_date=QDate(2013, 6, 7), closing_date=None,
        transaction_limit=None, account_type=AccountTypeData(name='studenckie', version=4))
    assert account == correct

def test_account_to_outside(database):
    transakcje = TransactionOutsideData.load_all(database)
    first = transakcje[0]
    account = first.account_to(database)
    correct = OutsideAccountData(
        outside_account_id=1, account_nr='11101025890123456789123456',
        bank=BankData(bank_id=1, name='Bank Spółdzielczy', NIP='1234567890',
                      address=AddressData(country='Polska', city='Poznań',
                                          post_code='60-011', street='Kwiatowa',
                                          house_nr='1', apartment_nr=None)))
    assert account == correct


if __name__ == "__main__":
    with testing_database() as database:
        test_transakcje_wewnetrzne_load(database)
        test_transakcje_zewnetrzne_load(database)
        test_account_from(database)
        test_account_to_inside(database)
        test_account_to_outside(database)