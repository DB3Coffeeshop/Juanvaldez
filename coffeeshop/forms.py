from django.forms import ModelForm, NumberInput, TextInput, Select, DateTimeInput, CheckboxInput
from django import forms
from coffeeshop.models import City, Departament, Client, Product, Product_type, Provider, Sale, Bill_payment, Description_bill_payment

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

class Sale_form(forms.ModelForm):
	
	class Meta:
		model = Sale
		fields = ('id_sale', 'quantity_sold', 'id_product')

		widgets = {
			'id_sale': forms.NumberInput(attrs={'class': 'form_sale'}),
			'quantity_sold': forms.NumberInput(attrs={'class': 'form_sale'}),
			'id_product': forms.Select(attrs={'class': 'form_sale'}),
			#'sale_value': forms.NumberInput(attrs={'class': 'form_sale'}),

		}

		labels = {
			'id_sale': 'ID venta',
			'quantity_sold': 'Cant vendida',
			'id_product': 'Producto',
			'sale_value': 'Val venta',
	}

class Bill_form(forms.ModelForm):

	class Meta:
		model = Bill_payment
		fields = ('id_bill_payment', 'id_client')

		widgets = {
			'id_bill_payment': forms.NumberInput(attrs={'class': 'form_bill'}),
			'id_client': forms.Select(attrs={'class': 'form_bill'}),
			#'payment_date': forms.DateTimeInput(attrs={'class': 'form_bill'}),
		}

		labels = {
			'id_bill_payment': 'ID factura',
			'id_client': 'Cliente',
			#'payment_date': 'Fecha',
		}


class Description_bill_form(forms.ModelForm):

	class Meta:
		model = Description_bill_payment
		fields = ('id_payment', 'pay_mode', 'employee_name')

		widgets = {
			'id_payment': forms.NumberInput(attrs={'class': 'form_description'}),
			'pay_mode': forms.Select(attrs={'class': 'form_description'}),
			'employee_name': forms.TextInput(attrs={'class': 'form_description'}),
		}

		labels = {
			'id_payment': 'ID factura',
			'pay_mode': 'Modo pago',
			'employee_name': 'Nombre empleado',
		}

class Client_form(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('name_client', 'id_client', 'id_city')

		widgets = {
			'name_client': forms.TextInput(attrs={'class': 'form_client'}),
			'id_client': forms.NumberInput(attrs={'class': 'form_client'}),
			'id_city': forms.Select(attrs={'class': 'form_client'}),
		}

		labels = {
			'name_client': 'Nombre',
			'id_client': 'CC',
			'id_city': 'Ciudad',
		}
