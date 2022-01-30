# apps/newsmag/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.newsmag.models import Category 

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name','publish', 'status')
	list_filter = ('status', 'created', 'publish', 'name')
	search_fields = ('name',)
	prepopulated_fields = {'slug': ('name',)}
	date_hierarchy = 'publish'
	ordering = ('status', 'publish')
