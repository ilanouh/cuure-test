# Cuure Challenge

# Quick Setup

> Prerequisites:
>
> - virtualenvwrapper
> - python3

```
# Create virtualenv
mkvirtualenv --python=`which python3` cuure -r requirements.txt
# Create db
./manage.py migrate
# Populate DB
./manage.py populate_db
# Run server
./manage.py runserver
```

You can connect using username `admin` and password `password` on `auth/login/`.
Endpoints are `api/notes/` and `api/patients/`, where you can list all notes and patients associated to the connected User (nutritionist). You can also create a Patient or a Note using the same endpoints with a POST request.
I've focused on a DRF backend to implement the views, rather than a frontend, that could easily be implemented later on using the API, using frontend frameworks such as React or even Django's HTML templates.
