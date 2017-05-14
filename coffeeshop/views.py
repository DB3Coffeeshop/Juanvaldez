from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
#from django.http import HttpResponseNotFound, HttpResponse
from .forms import Product_form, Product_type_form
from .models import Product, Product_type, Promotion



class Product_list(ListView):
	model = Product
	template_name = 'coffeeshop/Pr.html'


def description_view(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'coffeeshop/product_description.html', {'product': product})


def user_view(request):
	return render(request, 'coffeeshop/user-base.html')


def h1(request):
	return render(request, 'coffeeshop/h1.html')


def h2(request):
	return render(request, 'coffeeshop/h2.html')


def h3(request):
	return render(request, 'coffeeshop/h3.html')


def h4(request):
	return render(request, 'coffeeshop/h4.html')


def view_register_sell(request):
	return render(request, 'coffeeshop/register_sell.html')


def view_register_admin(request):
	return render(request, 'coffeeshop/add_client.html')


def view_check_product(request):
	return render(request, 'coffeeshop/check_sells.html')


def promotions_combos_view(request):
	return render(request, 'coffeeshop/promotions_combs.html')


def product_add_view(request):
	if request.method == 'POST':
		product_form = Product_form(request.POST) 

		if product_form.is_valid():
			form = product_form.save(commit=False)
			form.save()
			html = '<h1>Thanks</h1>'
			return HttpResponse(html)
	else:
		product_form = Product_form()

	return render(request, 'coffeeshop/add_product.html', {'form': product_form})


class Product_add(CreateView):
	model = Product
	form_class = Product_form
	template_name = 'coffeeshop/add_product.html'
	success_url = reverse_lazy('coffeeshop:index')
