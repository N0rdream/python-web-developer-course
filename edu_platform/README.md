# Edu-Platform

About
----------
Edu-Platform is a simple web application to store and show information about courses and teachers.  
Application is built with Django and Django REST framework.

Examples
----------------


Installation
-----------
```
$ git clone https://github.com/N0rdream/python-web-developer-course.git
$ cd python-web-developer-course/edu-platform
```

Dependencies & requirments
----------
Check requirments.txt file for dependencies.    
Edu-Platform runs with Python 3.6+.

How to run
-------------
Set SECRET_KEY enviroment variable. For example:   
```
$ export SECRET_KEY="top_secret"
```
   
Create database: 
```
$ python manage.py migrate
```
Create superuser for admin panel: 
```
$ python manage.py createsuperuser
```
Run server: 
```
$ python manage.py runserver
```
Type in browser for all API routes:  
```
http://localhost:8000/api
```

Examples
---------------------
Output for "teachers":
```
[
    {
        "id": 1,
        "user": {
            "first_name": "Илья",
            "last_name": "Лебедев"
        },
        "description": "Эксперт, консультант по архитектуре приложений."
    },
    {
        "id": 2,
        "user": {
            "first_name": "Юрий",
            "last_name": "Дворжецкий"
        },
        "description": "Ведущий разработчик в Luxoft, кандидат физико-математических наук."
    }
]
```
Output for "course":
```
{
    "id": 1,
    "title": "Web-разработчик на Python",
    "description": "Цель курса “WEB-разработка на Python” – подготовить специалиста, который сможет не только решать рядовые задачи бекенд-разработки, но и сделать с нуля современную фронтенд часть.",
    "price": 40000,
    "group": 1,
    "link": "https://otus.ru/lessons/webpython/",
    "lections": [
        {
            "title": "Занятие 1",
            "description": "Технические детали курса; декомпозиция; чистые функции...",
            "date": "2018-02-13"
        },
        {
            "title": "Занятие 2",
            "description": "Объекты и переменные; структуры данных...",
            "date": "2018-03-05"
        },
        {
            "title": "Занятие 3",
            "description": "Принципы ООП; mixins; class/instance variables...",
            "date": "2018-03-12"
        }
    ],
    "teachers": [
        {
            "user": {
                "first_name": "Илья",
                "last_name": "Лебедев"
            },
            "description": "Эксперт, консультант по архитектуре приложений."
        },
        {
            "user": {
                "first_name": "Юрий",
                "last_name": "Дворжецкий"
            },
            "description": "Ведущий разработчик в Luxoft, кандидат физико-математических наук."
        }
    ]
}
```

Database
---------------------
You can use Django admin panel to add new entities to database:   
```
http://localhost:8000/admin
```
Notes
-----------
Edu-Platform is written for educational purpose.