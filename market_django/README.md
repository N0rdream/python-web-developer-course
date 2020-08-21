# Django-Market

About
----------
Django-Market is a simple web application to store and show information about different products.  
Application is built with Django and SQLite database.

How it looks
----------------
Index page example:
![Index page example](/example/index.png)
 
Product category page example:
![Product category page example](/example/category.png)

Product page example:
![Product page example](/example/product.png)

Database scheme
--------------------
![Database scheme](/example/schema.png)

Installation
-----------
```
$ git clone https://github.com/N0rdream/Django-Market.git
$ cd Django-Market
```

Dependencies & requirments
----------
Check requirments.txt file for dependencies.    
Django-Market runs with Python 3.6+.

How to run
-------------
Set SECRET_KEY enviroment variable. For example:   
```
$ export SECRET_KEY="top_secret"
```
   
Create database: 
```
python manage.py migrate
```
Create superuser for admin panel: 
```
python manage.py createsuperuser
```
Run server: 
```
python manage.py runserver
```
Type in browser:  
```
http://localhost:8000/catalog
```
Database
---------------------
You can use Django admin panel to add new products to database:   
```
http://localhost:8000/admin
```
Notes
-----------
Django-Market is written for educational purpose.