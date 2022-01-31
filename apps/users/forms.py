# apps/users/forms.py

# Django modules
from django import forms

# Locals

# Create your forms here.


# FORM: UserLoginForm
class UserLoginForm(forms.Form):
	email = forms.CharField(
		widget=forms.EmailInput(attrs={
		'class': 'form-control'
		})
	)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
		'class': 'form-control'
		})
	)
