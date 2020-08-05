
# Developing Django on Repl.it

- Fork this template to get started
- Simply hit run to start the server
- The server will autoreload as needed. You don't need to restart the server manually.

## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/


# drf-learns
Simple training ground based on Django rest framework

Links for training:
https://webdevblog.ru/razrabotka-na-osnove-testov-django-restful-api/
https://stackoverflow.com/questions/47184777/how-to-login-a-user-during-a-unit-test-in-django-rest-framework/47184778
<<<<<<< HEAD
https://stackoverflow.com/questions/23072730/django-rest-framework-how-to-test-viewset
https://stackoverflow.com/questions/2342579/http-status-code-for-update-and-delete
Python testing
https://habr.com/ru/post/269759/
Vue & Auth links
https://blog.sqreen.com/authentication-best-practices-vue/
https://auth0.com/docs/tokens/concepts/token-storage
=======
https://stackoverflow.com/questions/23072730/django-rest-framework-how-to-test-viewset
>>>>>>> 520291b2b15db9c48bf562f464a1c1b8761d8a3b
