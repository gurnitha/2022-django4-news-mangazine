# apps/accounts/forms.py

# Django modules
from django import forms
from django.contrib.auth.models import User

# Locals
from apps.accounts.models import Profile

# Create your forms here.


# FORM: UserRegistrationForm
class UserRegistrationForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')

	first_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'form-control'
		}))

	last_name = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'form-control'
		}))

	username = forms.CharField(
		widget=forms.TextInput(attrs={
			'class': 'form-control'
		}))

	email = forms.CharField(
		widget=forms.EmailInput(attrs={
		'class': 'form-control'
		})
	)

	password = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'class': 'form-control'
		}))

	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={
			'class': 'form-control'
		}))

	# widgets = {
	# 	'first_name': forms.TextInput(
	# 		attrs={'class': 'form-control'}
	# 	),
	# 	'last_name': forms.TextInput(
	# 		attrs={'class': 'form-control'}
	# 	),
	# 	'email': forms.EmailInput(
	# 		attrs={'class': 'form-control'}
	# 	),
	# 	'password': forms.PasswordInput(
	# 		attrs={'class': 'form-control'}
	# 	),
	# }


	
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


# FORM: UserUpdateForm
class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

		# first_name = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))

		# last_name = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))

		# username = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 		'class': 'form-control'
		# 	}))

		# email = forms.CharField(
		# 	widget=forms.EmailInput(attrs={
		# 	'class': 'form-control'
		# 	})
		# )

		widgets = {
			'first_name': forms.TextInput(
				attrs={'class': 'form-control'}
			),
			'last_name': forms.TextInput(
				attrs={'class': 'form-control'}
			),
			# 'username': forms.TextInput(
			# 	attrs={'class': 'form-control'}
			# ),
			'email': forms.EmailInput(
				attrs={'class': 'form-control'}
			)
		}


# FORM: UserUpdateProfileForm
class UserUpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('phone_number', 'address', 'postal_code', 'city', 'country')

		# phone_number = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))

		# email = forms.CharField(
		# 	widget=forms.EmailInput(attrs={
		# 	'class': 'form-control'
		# }))
		
		# address = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))

		# postal_code = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))

		# city = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))

		# country = forms.CharField(
		# 	widget=forms.TextInput(attrs={
		# 	'class': 'form-control'
		# }))


		widgets = {
			'phone_number': forms.TextInput(
				attrs={'class': 'form-control'}
			),
			'address': forms.TextInput(
				attrs={'class': 'form-control'}
			),

			# 'email': forms.TextInput(
			# 	attrs={'class': 'form-control'}
			# ),
			'postal_code': forms. TextInput (
				attrs={'class': 'form-control'}
			),
			'city': forms. TextInput (
				attrs={'class': 'form-control'}
			),
			'country': forms. TextInput (
				attrs={'class': 'form-control'}
			)
		}


