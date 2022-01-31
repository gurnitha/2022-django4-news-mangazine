# apps/users/urls.py

# Django modules
from django.urls import path
from django.contrib.auth import views as auth_views

# Locals
from apps.users.views import *

app_name = 'users'
urlpatterns = [
	path('login/', UserLoginView, name='user_login'),
	path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
	path('register/', UserRegisterView, name='user_register'),

]