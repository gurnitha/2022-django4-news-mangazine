# apps/newsmag/forms.py

# Django modules
from django import forms
from apps.newsmag.models import Category

# Create your forms here.

# ModelForm:CategoryCreate
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'