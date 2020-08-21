def construct_drop_table_sql(tablename):
    return f'DROP TABLE IF EXISTS {tablename}'


def construct_create_table_sql(tablename, fields):
    result = []
    for k, v in fields.items():
        line = f'{k} {v.sql_type}'
        if v.primary_key:
            line += ' PRIMARY KEY'
        if v.required:
            line += ' NOT NULL'
        result.append(line)
    cols = ', '.join(result)
    return f'CREATE TABLE IF NOT EXISTS {tablename} ({cols})'


def construct_insert_sql(tablename, cols_list):
    cols = ', '.join(cols_list)
    values = ", :".join(cols_list)
    return f'INSERT INTO {tablename} ({cols}) VALUES (:{values})'


def construct_select_sql(tablename, cols_list):
    cols = ', '.join(cols_list) if cols_list else '*'
    return f'SELECT {cols} FROM {tablename}'


def construct_update_sql(tablename, cols_list, params_list):
    cols = ', '.join(f'{c} = :{c}' for c in cols_list)
    params = ' AND '.join(f'{p} = :{p}' for p in params_list)
    return f'UPDATE {tablename} SET {cols} WHERE {params}'