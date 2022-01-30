# apps/newsmag/views.py

# Django modules
from django.shortcuts import render

# Locals

# Create your views here.


# VIEW:HomePageView
def HomePageView(request):
	return render(request, 'newsmag/index.html')