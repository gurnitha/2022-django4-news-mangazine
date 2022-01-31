# apps/users/views.py

# Django modules
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

# Locals
from apps.users.forms import UserLoginForm

# Create your views here.


''' Logic of the UserLoginView
    --------------------------

    1. 	First, and for most, to understand that Django App colled 'auth', comes with
       	default User's attributes, such as:
       	- username,
       	- email,
       	- password, etc.
    
    2. 	We will make use of that existing attributes, to make user to be able to login
       	to the app.
    
    3. 	To do so, we need to create a new file inside the users app called 'forms.py'.
       	Inside it, we have to add a form. The form makes use 'username, and password'
       	exist in the auth app. We named the form as UserLoginForm.
	
	4. 	One the form is ready, then we import it to the views to be loaded in the
	    UserLoginView method. 

	5. 	One the login in UserLoginView is defined, it will work as follows:

	5.1 If the app receives the GET request, that is, when a user visits the login page
		without submitting anything, the app simply renders the login form/login.html template. 

	5.2 When a user submits data using the POST method, the app instantiates, 
		validate, and clean the form. The app then looks for the user record based on 
		the email provided. 

	5.3 If no such user is found, the app raises the Model.DoesNotExist exception and render
		login.html template again. We could also use the shortcut function
		get_object_or_404() to handle this, but we don’t want to throw a 404 error at
		the user.

	5.4 If a record with the provided email exists, the app tries to verify user credentials
		using authenticate() provided by the Django authentication framework.
	
	5.5 Once a user is successfully verified, authenticate() returns User object, 
		attached to it to the current session by using login() function and redirect to our
		landing page or the home page.

	6. 	To make them working, we have to load the UserLoginView's "form" instance in the 
		login.html. 

	7. 	The last thing to do is to add in settings.py file the LOGIN_URL='app_name.login',
	    in this case LOGIN_URL = 'users.login'. It is important to note, that is we named
	    the url as 'users'. If we did not name the url, we simply add the LOGIN_URL to
	    settings.py as this LOGIN_URL='login'.

	8. 	Once those things done, we can try it out and check the result.
'''

# ============== USER LOGIN, REGISTER AND LOGOUT ==============

# VIEW: UserLoginView
def UserLoginView(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			clean_form = form.cleaned_data
			user_record = None
			try:
				user_record = User.objects.get(email=clean_form['email'])
			except User.DoesNotExist:
				pass 

			if user_record:
				user = authenticate(
					request,
					username=user_record,
					password=clean_form['password']
				)

				if user is not None:
					login(request, user)
					return redirect('newsmag:homepage')

			messages.error(request, 'Incorrect email / password')

	else:
		form = UserLoginForm()

	context = {'form':form}
	return render(request, 'users/login.html', context)


# ============== END USER LOGIN, REGISTER AND LOGOUT ==========
