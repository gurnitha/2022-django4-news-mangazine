# apps/newsmag/views.py

# Django modules
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Locals
from apps.newsmag.forms import CategoryCreateForm
from apps.newsmag.models import Category

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
		return render(request, 'newsmag/category_create.html', context)


# VIEW: CategoryUpdateView
def CategoryUpdateView(request, category_id):

	category_id = int(category_id)

	try:
		cat_sel = Category.objects.get(id = category_id)
	except Category.DoesNotExist:
		return redirect('newsmag:homepage')

	cat_form = CategoryCreateForm(request.POST or None, instance = cat_sel)
	if cat_form.is_valid():
		cat_form.save()
		return redirect('newsmag:homepage')

	context = {'form':cat_form}
	return render(request, 'newsmag/category_update.html', context)


