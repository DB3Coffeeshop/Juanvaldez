from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
#from django.http import HttpResponseNotFound, HttpResponse
from .forms import Product_form, Product_type_form
from .models import Product, Product_type


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
	return render(request, 'coffeeshop/admin-registrar_venta.html')
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

def index(request):
	if request.method == 'POST':
		type_form = Product_type_form(request.POST)
		product_form = Product_form(request.POST) 

		if type_form.is_valid() and product_form.is_valid():
			form = type_form.save()
			print (form.id_product_type)
			form_2 = product_form.save(commit=False)
			get_type = Product_type.objects.get(pk=form.id_product_type)
			print (get_type.id_product_type)
			form_2.id_provider = get_type
			form_2.save()
			html = '<h1>Thanks</h1>'
			return HttpResponse(html)
	else:
		product_form = Product_form()
		type_form = Product_type_form()

	return render(request, 'coffeeshop/form_example.html', {'form': product_form, 'form_2': type_form})
