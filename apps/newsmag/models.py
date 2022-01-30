# apps/newsmbag/models.py

# Django modules
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

# MODEL:Category
class Category(models.Model):

    STATUS_CATEGORY_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    name = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, choices=STATUS_CATEGORY_CHOICES, default='draft')

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']
