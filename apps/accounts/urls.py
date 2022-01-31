# apps/accounts/urls.py

# Django modules
from django.urls import path
from django.contrib.auth import views as auth_views

# Locals
from apps.accounts.views import *

# app_name = 'accounts'
urlpatterns = [
	path('login/', UserLoginView, name='user_login'),
	path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
	path('register/', UserRegisterView, name='user_register'),
	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	
]