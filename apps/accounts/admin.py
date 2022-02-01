# apps/accounts/models.py

# Django modules
from django.contrib import admin

# Locals
from apps.accounts.models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['user', 'phone_number', 'address', 'postal_code', 'city']