from django.forms import ModelForm
from django import forms
from coffeeshop.models import City, Departament, Client, Product, Product_type

class Product_form(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('id_product', 'name_product', 'price', 'stock', 'id_promotion', 'id_product_type', 'id_provider')


class Product_type_form(forms.ModelForm):

	class Meta:
		model = Product_type
		fields = ('id_product_type', 'product_type', 'product_description', 'id_promotion')
	
	

