# SQLMetaphysics


About
----------
SQLMetaphysics is a simple object-relational mapper (ORM) for sqlite3 Python library.

Installation
-----------
```
$ git clone https://github.com/N0rdream/SQLMetaphysics.git
$ cd SQLMetaphysics 
```

Dependencies & requirments
----------
For dependencies check requirements.txt.
SQLMetaphysics runs with Python 3.6+.  


Usage
-------------
1. Initialize database:
```
from SQLMetaphysics import models, fields, connection

models.Model.db = connection.DatabaseConnection('test.db')
```
   
2. Create models to interact with tables in database:
```
class Laptop(models.Model):
    __tablename__ = 'notebooks'
    id = fields.Integer(primary_key=True)
    brand = fields.Text(required=True)
    price = fields.Real(required=True)
    year = fields.Integer()
```
SQLMetaphysics supports 3 datatypes: INTEGER, REAL and TEXT.  
  
3. Create table in database:
```
Laptop.create()
```
Or you can create all tables simultaneously:  
```
Model.create_all()
```
   
4. Insert data:
```
Laptop(brand='Blueberry', price=1999.99).insert()
Laptop(brand='Blueberry', price=999, year=2017).insert()
Laptop(brand='Celery', price=1999.99, year=2018).insert()
```
  
Or update data:
```
# UPDATE notebooks SET year = 2018 WHERE brand = 'Blueberry' AND price = 1999.99
Laptop(year=2018).update(brand='Blueberry', price=1999.99)
```
   
5. Select data:
```
# SELECT * FROM notebooks
data = Laptop.select()

#SELECT price, year FROM notebooks
data = Laptop.select('price', 'year')
```
   
6. For drop database use:
```
Laptop.drop()
```
   
Or you can drop all tables simultaneously:  
```
Model.drop_all()
```

Tests
-----------
Just run:
```
pytest
```

 
Notes
-----------
SQLMetaphysics is written for educational purpose.
It is not suited for production.