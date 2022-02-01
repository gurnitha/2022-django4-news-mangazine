# apps/accounts/views.py

# Django modules
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Locals
from apps.accounts.forms import (
	UserLoginForm, 
	UserRegistrationForm,
	UserUpdateForm,
	UserUpdateProfileForm)
from apps.accounts.models import Profile

# Create your views here.


# ============== USER REGISTER, LOGIN, AND LOGOUT ==============

''' Logic of the UserRegisterView
	-----------------------------

	1. When the UserRegistrationForm form is submitted via 
	POST action, we instantiate, validate, and clean it. 

	2. During the registration process, a user submits the 
	password twice. 
	
	3. If the provided passwords don’t match, we send
	back an error message informing the user about this issue. 

	4. If the passwords match, we check if a user with the 
	provided email already exists. 

	5. If a user with this email already exists, we let the user 
	know via an error message. 

	6. In case no issues arise, we proceed to the user creation 
	and render the register_done.html template.

'''

# VIEW: UserRegisterView
def UserRegisterView(request):

	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			clean_form = user_form.cleaned_data

			email = clean_form['email']
			password = clean_form['password']
			password2 = clean_form['password2']

			if password == password2:
				if User.objects.filter(email=email).exists():
					messages.error(request,
						'User with given email already exists')
					return render(
						request,
						'accounts/register.html',
						{'user_form': user_form}
					)
			else:
				messages.error(request, 'Passwords don\'t match')
				return render(
					request,
					'accounts/register.html',
					{'user_form': user_form}
				)

			# Create a new user object
			new_user = User.objects.create_user(
				first_name=clean_form['first_name'],
				last_name=clean_form['last_name'],
				username=clean_form['username'],
				email=email,
				password=password
			)

			# Create the user profile
			Profile.objects.create(user=new_user)

			return render(
				request,
				'accounts/register_done.html',
				{'new_user': new_user}
			)

	else:
		user_form = UserRegistrationForm()

	context = {'form':user_form}
	return render(request, 'accounts/register.html', context)


''' Logic of the UserLoginView
    --------------------------

    1. 	First, and for most, to understand that Django App colled 'auth', comes with
       	default User's attributes, such as:
       	- username,
       	- email,
       	- password, etc.
    
    2. 	We will make use of that existing attributes, to make user to be able to login
       	to the app.
    
    3. 	To do so, we need to create a new file inside the accounts app called 'forms.py'.
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
	    in this case LOGIN_URL = 'accounts.login'. It is important to note, that is we named
	    the url as 'accounts'. If we did not name the url, we simply add the LOGIN_URL to
	    settings.py as this LOGIN_URL='login'.

	8. 	Once those things done, we can try it out and check the result.
'''

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
	return render(request, 'accounts/login.html', context)


# ============== END USER LOGIN, REGISTER AND LOGOUT ==========


# ========================== USER PROFILE =====================


''' The logic of Creating User Profile
    ----------------------------------
1. We have successfully extended our basic User model by implementing
Profile model. 

2. As for next step, let’s create a customer profile section. We
want to show user information there. This means showing data from both
User and Profile models. User will be also able to edit the account
information. 

3. We will create two forms to handle this functionality: UserUpdateForm and
UserUpdateProfileForm. 

Note: They are done already in apps/accounts/forms.py file.

4. Now move to accounts/views.py. We start by decorating our 
UserProfileView view with @login_required decorator,
which requires a user to be logged in. 

5. If a user is not logged in, this view redirects visitor to the login page.

6. But when a user logged in, and visits the profile page, we render 
an accounts/profile.html template and provide a profile form responsible 
for handling our user data.

7. This form is provided with the instance of existing User and Profile models
that are supposed to be displayed and updated if required.

8. When our form is submitted via a POST request, we first check if a user with
the given email already exists. 

9. If such user already exists, we check if it’s us.
If so, we then proceed and save our forms with associated User and Profile
instances.

10. Now we need to create a template for showing our profile page. Go ahead
and create a profile.html template inside the templates/accounts directory
within the accounts application. Add the following code to it:

11. Now we need to modify urls.py file in the account directory and add the
following URL pattern to the file:
apps/accounts/urls.py
#...
path('profile/', views.profile, name='profile'),

12. And finally, add our profile URL to the navbar 

#...
 {% if request.user.is_authenticated %}
<li>
    <i class="bx bx-user"></i>
    <a href="{% url 'user_profile' %}">{{ request.user.username }}</a>
</li>
# ...

13. Make sure the local development server is running and visit
http://127.0.0.1:8000/. The email address in the navbar will contain a link to
the user profile. 

14. Go ahead and click on that link. You will see:
We are greeted with the exception RelatedObjectDoesNotExist. 

Well, what does that mean? 

Check the exception value below that; User has no profile.
Remember that our associated profile is created upon user creation. We have
created our superuser at the beginning of the project, long before our Profile
model. Let’s remedy this issue. Open
http://127.0.0.1:8000/admin/accounts/profile/add/ and create Profile record
manually:

Select a user from the dropdown, fill in required data, and click on Save:

15. Now let’s try to access the profile page
http://127.0.0.1:8000/accounts/profile/ again. We are greeted with a profile
page. It contains all User and Profile information along with an Update
profile and Change password links:

16. Let’s test our Update profile functionality. Fill in some new data and click on
the Update profile link. After the profile update, we are also notified by a
success message:

17. If we tried to update the email address, which is already in our database and
used by another user, we would receive a following error message:

'''


# VIEW: UserProfileView
@login_required
def UserProfileView(request):

	if request.method == 'POST':
		email = request.POST['email']
		user = None

		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			pass

		if user is None or user.id == request.user.id:
			user_form = UserUpdateForm(
				instance=request.user,
				data=request.POST
			)

			profile_form = UserUpdateProfileForm(
				instance=request.user.profile,
				data=request.POST,
			)

			if user_form.is_valid() and profile_form.is_valid():
				user_form.save()
				profile_form.save()
				messages.success(request, 'Profile was updated successfully')
		
		else:
			messages.error(request, 'User with given email already exists')
		return redirect('user_profile')

	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = UserUpdateProfileForm(instance=request.user.profile)

	context = {
		'user_form': user_form,
		'profile_form': profile_form
	}

	return render(request, 'accounts/profile.html', context)

# ======================== ENDUSER PROFILE ====================
