# apps/newsmag/templatetags/custom_template.py

# Django modules
from django import template

# Locals
from apps.newsmag.models import Category

# Template library
register = template.Library()

# Register your template here
@register.inclusion_tag('shared/navbar/main_navbar.html')
def show_menu():
	categories = Category.objects.order_by('id')[0:4]
	categories_dropdown = Category.objects.order_by('id')[4:] 
	context = {
		'categories':categories,
		'categories_dropdown':categories_dropdown
	}
	return context
