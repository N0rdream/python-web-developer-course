class Field:
    def __set_name__(self, cls, name):
        self.name = name
    
    def __init__(self, primary_key=False, required=False):
        self.primary_key = primary_key
        self.required = required

    def __set__(self, instance, value):
        flag = [True for exp_type in self.expected_types if isinstance(value, exp_type)]
        if not flag:
            raise TypeError(f'Expected {self.expected_types} for {value} in {instance.__class__.__name__}')
        instance.__dict__[self.name] = value


class Integer(Field):
    sql_type = 'INTEGER'
    expected_types = [int]


class Real(Field):
    sql_type = 'REAL'
    expected_types = [int, float]


class Text(Field):
    sql_type = 'TEXT'
    expected_types = [str]