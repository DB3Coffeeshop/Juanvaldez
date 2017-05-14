from django.forms import ModelForm, NumberInput, TextInput, Select
from django import forms
from coffeeshop.models import City, Departament, Client, Product, Product_type

class Product_form(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('id_product', 'name_product', 'price', 'stock', 'id_promotion', 'id_product_type', 'id_provider')	
		widgets = {
			'id_product': forms.NumberInput(attrs={'class': 'form_class'}),
			'name_product': forms.TextInput(attrs={'class': 'form_class'}),
			'price': forms.NumberInput(attrs={'class': 'form_class'}),
			'id_promotion': forms.Select(attrs={'class': 'form_class'}),
			'stock': forms.NumberInput(attrs={'class': 'form_class'}),
			'id_product_type': forms.Select(attrs={'class': 'form_class'}),
			'id_provider': forms.Select(attrs={'class': 'form_class'}),
		}
	


class Product_type_form(forms.ModelForm):

	class Meta:
		model = Product_type
		fields = ('id_product_type', 'product_type', 'product_description', 'id_promotion')
	
	

