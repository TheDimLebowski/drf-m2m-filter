# Django-Rest-Framework many-to-many filtering test app

Trying to solve 

http://stackoverflow.com/questions/39368410/django-rest-framework-manytomany-filter-multiple-values/39368843#39368843

## Run:

```
pip install -r requirements.txt
createdb test
python manage.py migrate
python insert_data.py
python manage.py runserver
```

## Go to:

http://127.0.0.1:8000/api/users/?labels=1&labels=2

and hope you can only see users with labels 1 and 2.
