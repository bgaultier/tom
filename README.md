# TOM
TOM is a web platform for the *Fabriquer un objet connecté* MOOC.
It will allow the MOOC students to manipulate Nelson objects using a RESTful API directly from the edX FUN instance.

## Installation
1. [Install a LAMP server](http://wiki.debian.org/LaMp)
2. [Fork this repo](https://help.github.com/articles/fork-a-repo)
3. Install [Django](https://www.djangoproject.com) and [Django Rest Framework](http://django-rest-framework.org) using pip then start the server :  
```
$ cd tom/
$ sudo apt-get install pip
$ sudo pip install django djangorestframework
$ python manage.py makemigrations nelsons
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver 0.0.0.0:8000
```

## Endpoints

1. First, you have to create a nelson object using the admin : http://localhost:8000/admin/
2. Log in using the credentials for the super user
3. Create a Nelson object using the **Add** button
4. Then go to http://localhost:8000/nelsons/baptiste/ to enjoy the *Browseable API* offred by [Django Rest Framework](http://django-rest-framework.org)
