from .constructors import (
    construct_drop_table_sql,
    construct_create_table_sql,
    construct_insert_sql,
    construct_select_sql,
    construct_update_sql
)


def create_table_sql(database, tablename, fields):
    query = construct_create_table_sql(tablename, fields)
    with database as db:
        db.execute(query)
        db.commit()


def drop_table_sql(database, tablename):
    query = construct_drop_table_sql(tablename)
    with database as db:
        db.execute(query)
        db.commit()


def insert_sql(database, tablename, fields):
    query = construct_insert_sql(tablename, fields.keys())
    with database as db:
        db.execute(query, fields)
        db.commit()


def update_sql(database, tablename, cols, params):
    query = construct_update_sql(tablename, cols.keys(), params.keys())
    with database as db:
        db.execute(query, {**cols, **params})
        db.commit()


def select_sql(database, tablename, cols_list):
    query = construct_select_sql(tablename, cols_list)
    with database as db:
        return db.execute(query).fetchall()