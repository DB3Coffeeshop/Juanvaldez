from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
#from django.http import HttpResponseNotFound, HttpResponse
#from .forms import Dpto_form, Client_form
from .models import Product


def principal_view(request):
	list_products = Product.objects.all()
	context = {'list_products': list_products}
	return render(request, 'coffeeshop/Pr.html', context)


def description_view(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'coffeeshop/description.html', {'product': product})


def admin_view(request):
	return render(request, 'coffeeshop/user-base.html')


def h1(request):
	return render(request, 'coffeeshop/h1.html')


def h2(request):
	return render(request, 'coffeeshop/h2.html')


def h3(request):
	return render(request, 'coffeeshop/h3.html')


def h4(request):
	return render(request, 'coffeeshop/h4.html')


def view_x(request):
	pass
#def index(request):
#	if request.method == 'POST':
#		form = dpto_form(request.POST)
#		form_2 = client_form(request.POST) 

#		if form.is_valid() and form_2.is_valid():
#			post = form.save(commit = False)
#			post_2 = form_2.save(commit = False)
#			post.save()
#			post_2.save()
#			html = '<h1>Thanks</h1>'
#			return HttpResponse(html)
#	else:
#		form = dpto_form()
#		form_2 = client_form()
#
#	return render(request, 'coffeeshop/index.html', {'form': form, 'form_2': form_2})
