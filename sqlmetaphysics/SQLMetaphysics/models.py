from collections import namedtuple
from .queries import (
    insert_sql, 
    update_sql, 
    select_sql, 
    create_table_sql, 
    drop_table_sql
)
from .fields import Field


class ModelMeta(type):
    
    def __new__(meta, clsname, bases, clsdict):
        fields = {k: v for k, v in clsdict.items() if isinstance(v, Field)}
        if fields:
            clsdict['_fields'] = fields
        if '__tablename__' in clsdict:
            clsdict['_tablename'] = clsdict['__tablename__']
            del clsdict['__tablename__']
        else:
            clsdict['_tablename'] = clsname.lower()
        return super().__new__(meta, clsname, bases, clsdict) 
    
  
class Model(metaclass=ModelMeta):

    def __init__(self, **kwargs):
        if not kwargs:
            raise AttributeError('Expected at least 1 argument')
        for k, v in kwargs.items():
            if k in self._fields:
                setattr(self, k, v)
            else:
                raise KeyError(f'Bad column name: {k}')

    def insert(self):
        for k, v in self._fields.items():
            if v.required and not v.primary_key:
                if not k in self.__dict__:
                    raise AttributeError(f'Required argument <{k}> is missing')
        insert_sql(self.__class__.db, self._tablename, self.__dict__)

    def update(self, **kwargs):
        update_sql(self.__class__.db, self._tablename, self.__dict__, kwargs)

    @classmethod
    def select(cls, *args):
        for arg in args:
            if arg not in cls.__dict__:
                raise AttributeError(f'Table does not have <{arg}> field.')
        return select_sql(cls.db, cls._tablename, args)

    @staticmethod
    def create_all():
        for model in Model.__subclasses__():
            model.create()
    
    @staticmethod
    def drop_all():
        for model in Model.__subclasses__():
            model.drop()

    @classmethod
    def create(cls):
        Field = namedtuple('Field', ['sql_type', 'primary_key', 'required'])
        fields = {k: Field(v.sql_type, v.primary_key, v.required) for k, v in cls._fields.items()}
        create_table_sql(cls.db, cls._tablename, fields)

    @classmethod
    def drop(cls):
        drop_table_sql(cls.db, cls._tablename)