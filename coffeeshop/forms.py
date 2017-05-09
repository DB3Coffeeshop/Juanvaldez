from django.forms import ModelForm
from django import forms
from coffeeshop.models import City, Departament, Client, Product

class Product_form(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('id_product', 'name_product', 'price', 'stock')
		labels = {
			'id_dpto': ('id departament'),
			'dpto_name': ('name departament') 
		}

class Client_form(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('name_client', 'id_client', 'id_city')
	
	

