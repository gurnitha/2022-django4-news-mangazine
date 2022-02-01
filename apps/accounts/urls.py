# apps/accounts/urls.py

# Django modules
from django.urls import path
from django.contrib.auth import views as auth_views

# Locals
from apps.accounts.views import *

# app_name = 'accounts'
urlpatterns = [
	
	# Login, logout, register
	path('login/', UserLoginView, name='user_login'),
	path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),
	path('register/', UserRegisterView, name='user_register'),

	# Profile
	path('profile/', UserProfileView, name='user_profile'),

	# Password changed
	path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	
	# Password rest
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]