# Market-Flask

About
----------
Market-Flask is a simple 2-page web application to store and show information about laptops.
Application is built with Flask, SQLAlchemy and SQLite database.

How it looks
----------------
Index page example:
![Index page example](/_files/index_page.png)
  
  
Product page example:
![Product page example](/_files/product_page.png)

Database scheme
--------------------
![Database scheme](/_files/database_scheme.png)

Installation
-----------
```
$ git clone https://github.com/N0rdream/python-web-developer-course.git
$ cd python-web-developer-course/market-flask
```

Dependencies & requirments
----------
Check requirments.txt file for dependencies.  
Make sure to install the last version of Flask-admin:  
```pip install --upgrade git+https://github.com/flask-admin/flask-admin```  
Laptop-Market runs with Python 3.6+.

How to run
-------------
Set SECRET_KEY enviroment variable. For example:
```
$ export SECRET_KEY="top_secret"
```
Then run application:
```
python3 run.py
```
Type in browser: http://localhost:5000/notebooks

Database
---------------------
You can use Flask-Admin panel to add new laptop models to database:
http://localhost:5000/admin

Notes
-----------
Laptop-Market is written for educational purpose.