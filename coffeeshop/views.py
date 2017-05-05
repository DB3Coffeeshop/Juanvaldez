from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
#from django.http import HttpResponseNotFound, HttpResponse
from .forms import Dpto_form, Client_form
from .models import Product


def principal_view(request):
	list_products = Product.objects.all()
	context = {'list_products': list_products}
	return render(request, 'coffeeshop/Pr.html', context)


def description_view(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'coffeeshop/description.html', {'product': product})
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
