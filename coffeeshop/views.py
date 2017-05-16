from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
#from django.http import HttpResponseNotFound, HttpResponse
from .forms import Product_form, Product_type_form, Provider_form, Sale_form, Bill_form, Description_bill_form, Client_form
from .models import Product, Product_type, Promotion, Provider, Sale, Description_bill_payment, Bill_payment, Client



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


def view_check_product(request):
	return render(request, 'coffeeshop/check_sells.html')


def combos_view(request):
	return render(request, 'coffeeshop/combos.html')


class Client_table(ListView):
	model = Client
	template_name = 'coffeeshop/add_client.html'



class Client_register(CreateView):
	model = Client
	form_class = Client_form
	template_name = 'coffeeshop/client.html'
	success_url = reverse_lazy('coffeeshop:admin_register')



class product_table(ListView):
	model = Product
	template_name = 'coffeeshop/admin_products.html'


class Product_edit(UpdateView):
	model = Product
	second_model = Provider_form
	third_model = Product_type_form
	template_name = 'coffeeshop/add_product.html'
	success_url = reverse_lazy('coffeeshop:product_table')



class Product_add(CreateView):
	model = Product
	form_class = Product_form 
	second_form_class = Provider_form
	third_form_class = Product_type_form
	template_name = 'coffeeshop/add_product.html'
	success_url = reverse_lazy('coffeeshop:product_table')

	
	def get_context_data(self, **kwargs):
		context = super(Product_add, self).get_context_data(**kwargs)

		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)

		if 'form3' not in context:
			context['form3'] = self.third_form_class(self.request.GET)

		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		form3 = self.third_form_class(request.POST)

		if form.is_valid() and form2.is_valid() and form3.is_valid():
			product = form.save(commit=False)
			product.id_provider = form2.save()
			product.id_product_type = form3.save()
			product.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2, form3=form3))  


class Sell_product(CreateView):
	model = Sale
	form_class = Sale_form
	second_form_class = Bill_form
	third_form_class = Description_bill_form
	template_name = 'coffeeshop/register_sell.html'
	success_url = reverse_lazy('coffeeshop:index')


	def get_context_data(self, **kwargs):
		context = super(Sell_product, self).get_context_data(**kwargs)

		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)

		if 'form3' not in context:
			context['form3'] = self.third_form_class(self.request.GET)

		return context


	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		form3 = self.third_form_class(request.POST)

		if form.is_valid() and form2.is_valid() and form3.is_valid():
			sale = form.save(commit=False)
			bill = form2.save(commit=False)
			product_id = sale.id_product.id_product
			product = Product.objects.get(pk=product_id)
			product.stock -= sale.quantity_sold
			value = product.price * sale.quantity_sold
			product.save()
			id_client = bill.id_client.id_client
			client = Client.objects.get(pk=id_client)
			client.points += int(value)
			client.save()
			bill.id_payment = form3.save()
			sale.id_bill_payment = form2.save()
			sale.sale_value = value
			sale.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form,form2=form2,form3=form3))


class Client_delete(DeleteView):
	model = Client
	template_name = 'coffeeshop/client_delete.html'
	success_url = reverse_lazy('coffeeshop:admin_register')


class Product_delete(DeleteView):
	model = Product
	template_name = 'coffeeshop/product_delete.html'
	success_url = reverse_lazy('coffeeshop:product_table')


class Client_edit(UpdateView):
	model = Client
	form_class = Client_form
	template_name = 'coffeeshop/client.html'
	success_url = reverse_lazy('coffeeshop:admin_register')
