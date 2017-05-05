from django.forms import ModelForm
from django import forms
from coffeeshop.models import city, departament, client

class dpto_form(forms.ModelForm):

	class Meta:
		model = departament
		fields = ('id_dpto', 'dpto_name')
		labels = {
			'id_dpto': ('id departament'),
			'dpto_name': ('name departament') 
		}

class client_form(forms.ModelForm):

	class Meta:
		model = client
		fields = ('name_client', 'id_client', 'id_city')
	
	

