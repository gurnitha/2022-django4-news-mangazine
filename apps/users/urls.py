# apps/users/urls.py

# Django modules
from django.urls import path

# Locals
from apps.users.views import *

app_name = 'users'
urlpatterns = [
	path('login/', UserLoginView, name='user_login'),
]