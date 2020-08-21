from SQLMetaphysics import models, fields, connection


models.Model.db = connection.DatabaseConnection('test.db')

class Laptop(models.Model):
    __tablename__ = 'notebooks'
    id = fields.Integer(primary_key=True)
    brand = fields.Text(required=True)
    price = fields.Real(required=True)
    year = fields.Integer()


# CREATE TABLE IF NOT EXISTS notebooks
Laptop.create()

# INSERT INTO notebooks (brand, price) VALUES ('Blueberry', 1999.99)
# INSERT INTO notebooks (brand, price, year) VALUES ('Blueberry', 999, 2017)
# INSERT INTO notebooks (brand, price, year) VALUES ('Celery', 1999.99, 2018)
Laptop(brand='Blueberry', price=1999.99).insert()
Laptop(brand='Blueberry', price=999, year=2017).insert()
Laptop(brand='Celery', price=1999.99, year=2018).insert()

# UPDATE notebooks SET year = 2018 WHERE brand = 'Blueberry' AND price = 1999.99
Laptop(year=2018).update(brand='Blueberry', price=1999.99)
Laptop(year=2018, price=1999.99).update(brand='Blueberry')

# SELECT * FROM notebooks
data = Laptop.select()

# SELECT price, year FROM notebooks
data = Laptop.select('price', 'year')

# DROP TABLE IF EXISTS notebooks
Laptop.drop()






