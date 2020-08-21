from SQLMetaphysics.constructors import (
    construct_drop_table_sql,
    construct_create_table_sql,
    construct_insert_sql,
    construct_select_sql,
    construct_update_sql
)
from collections import namedtuple


def test_construct_drop_table_sql():
    assert construct_drop_table_sql('table') == 'DROP TABLE IF EXISTS table'


def test_construct_create_table_sql():
    Field = namedtuple('Field', ['sql_type', 'primary_key', 'required'])
    fields = {
        'id': Field('INTEGER', True, False),
        'brand': Field('TEXT', False, False), 
        'year': Field('INTEGER', False, True)
    }
    expected_result = 'CREATE TABLE IF NOT EXISTS notebooks ' \
    '(id INTEGER PRIMARY KEY, brand TEXT, year INTEGER NOT NULL)'
    assert construct_create_table_sql('notebooks', fields) == expected_result


def test_construct_insert_sql():
    cols_list = ['brand', 'price', 'year']
    expected_result = 'INSERT INTO notebooks (brand, price, year) ' \
    'VALUES (:brand, :price, :year)'
    assert construct_insert_sql('notebooks', cols_list) == expected_result


def test_construct_select_sql_all():
    assert construct_select_sql('name', []) == 'SELECT * FROM name'


def test_construct_select_sql():
    actual_result = construct_select_sql('name', ['price', 'year'])
    assert actual_result == 'SELECT price, year FROM name'


def test_construct_update_sql_case_one():
    actual_result = construct_update_sql("notebooks", ['year'], ['brand', 'price'])
    expected_result = 'UPDATE notebooks SET year = :year ' \
    'WHERE brand = :brand AND price = :price'
    assert actual_result == expected_result


def test_construct_update_sql_case_two():
    actual_result = construct_update_sql("notebooks", ['year', 'price'], ['brand'])
    expected_result = 'UPDATE notebooks SET year = :year, price = :price ' \
    'WHERE brand = :brand'
    assert actual_result == expected_result