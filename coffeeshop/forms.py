from django.forms import ModelForm, NumberInput, TextInput, Select
from django import forms
from coffeeshop.models import City, Departament, Client, Product, Product_type, Provider

class Product_form(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('id_product', 'name_product', 'price', 'stock', 'id_promotion')	
		widgets = {
			'id_product': forms.NumberInput(attrs={'class': 'form_product'}),
			'name_product': forms.TextInput(attrs={'class': 'form_product'}),
			'price': forms.NumberInput(attrs={'class': 'form_product'}),
			'id_promotion': forms.Select(attrs={'class': 'form_product'}),
			'stock': forms.NumberInput(attrs={'class': 'form_product'}),
			#'id_product_type': forms.Select(attrs={'class': 'form_class'}),
			#'id_provider': forms.Select(attrs={'class': 'form_class'}),
		}

		labels = {
			'id_product': 'ID producto',
			'name_product': 'Nombre producto',
			'price': 'Precio',
			'stock': 'Cantidad',
			'id_promotion': 'Promocion',
			#'id_provider': 'Proveedor',
			#'id_product_type': 'Tipo producto',
		}
	


class Product_type_form(forms.ModelForm):

	class Meta:
		model = Product_type
		fields = ('id_product_type', 'product_type', 'product_description', 'id_promotion')

		widgets = {
			'id_product_type': forms.NumberInput(attrs={'class': 'form_type'}),
			'product_type': forms.TextInput(attrs={'class': 'form_type'}),
			'product_description': forms.TextInput(attrs={'class': 'form_type'}),
			'id_promotion': forms.Select(attrs={'class': 'form_type'}),
		}

		labels = {
			'id_product_type': 'ID tipo producto',
			'product_type': 'Tipo producto',
			'product_description': 'Descripcion producto',
			'id_promotion': 'Promocion',
		}


class Provider_form(forms.ModelForm):

	class Meta:
		model = Provider
		fields = ('id_provider', 'provider_name', 'tel_provider', 'id_city') 

		widgets = {
			'id_provider': forms.NumberInput(attrs={'class': 'form_provider'}),
			'provider_name': forms.TextInput(attrs={'class': 'form_provider'}),
			'tel_provider': forms.NumberInput(attrs={'class': 'form_provider'}),
			'id_city': forms.Select(attrs={'class': 'form_provider'}),

		}

		labels = {
			'id_provider': 'ID proveedor',
			'provider_name': 'Nombre proveedor',
			'tel_provider': 'Telefono',
			'id_city': 'Ciudad',
		}
