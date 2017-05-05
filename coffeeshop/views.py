from django.shortcuts import render, redirect
from django.views.generic import ListView
#from django.http import HttpResponseNotFound, HttpResponse
from .forms import Dpto_form, Client_form
from .models import Product


class principal_view(ListView):
	context_object_name = 'list_products'
	queryset = Product.objects.all()
	template_name = 'coffeeshop/Pr.html'
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
