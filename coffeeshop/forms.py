from django.forms import ModelForm
from django import forms
from coffeeshop.models import City, Departament, Client

class Dpto_form(forms.ModelForm):

	class Meta:
		model = Departament
		fields = ('id_dpto', 'dpto_name')
		labels = {
			'id_dpto': ('id departament'),
			'dpto_name': ('name departament') 
		}

class Client_form(forms.ModelForm):

	class Meta:
		model = Client
		fields = ('name_client', 'id_client', 'id_city')
	
	

