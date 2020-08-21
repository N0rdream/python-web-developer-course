# Django-Market

About
----------
Django-Market is a simple web application to store and show information about different products.  
Application is built with Django and SQLite database.

How it looks
----------------
Index page example:
![Index page example](/_files/index.png)
 
Product category page example:
![Product category page example](/_files/category.png)

Product page example:
![Product page example](/_files/product.png)

Database scheme
--------------------
![Database scheme](/_files/schema.png)

Installation
-----------
```
$ git clone https://github.com/N0rdream/python-web-developer-course.git
$ cd python-web-developer-course/market-django
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