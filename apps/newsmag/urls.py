# apps/newsmag/urls.py

# Django modules
from django.urls import path

# Locals
from apps.newsmag.views import *

app_name = 'newsmag'
urlpatterns = [
	path('', HomePageView, name='homepage'),

	# CRUD:Category
	path('create-category/', CategoryCreateView, name='create_category')
]