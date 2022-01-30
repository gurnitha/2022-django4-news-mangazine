# apps/newsmag/urls.py

# Django modules
from django.urls import path

# Locals
from apps.newsmag.views import *

app_name = 'newsmag'
urlpatterns = [
	path('', HomePageView, name='homepage'),

	# CRUD:Category
	path('category-create/', CategoryCreateView, name='category_create'),
	path('category-update/<int:category_id>/', CategoryUpdateView, name='category_update'),
]