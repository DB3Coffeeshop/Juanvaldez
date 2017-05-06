from django.conf.urls import url

from . import views


app_name = 'coffeeshop'
urlpatterns = [

	url(r'^$', views.principal_view, name='index'),
	url(r'^product/(?P<product_id>[0-9]+)$', views.description_view, name ='product'),
]
