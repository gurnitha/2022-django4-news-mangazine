# apps/newsmag/views.py

# Django modules
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Locals
from apps.newsmag.forms import CategoryCreateForm

# Create your views here.


# VIEW:HomePageView
def HomePageView(request):
	return render(request, 'newsmag/index.html')


# CRUD: MAIN NAVBAR/CATEGORIES

def CategoryCreateView(request):
	
	cat_create = CategoryCreateForm()

	if request.method == 'POST':
		cat_create = CategoryCreateForm(request.POST)

		if cat_create.is_valid():
			cat_create.save()
			return redirect('newsmag:homepage')

		else:
			return HttpResponse("""Something went wrong, try again <a href="{{ url:'newsmag:homepage'}}">reload</a>""")

	else:
		context = {'form':cat_create}
		return render(request, 'newsmag/create_category.html', context)