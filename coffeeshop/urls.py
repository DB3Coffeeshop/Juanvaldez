from django.conf.urls import url

from coffeeshop.views import *
from . import views

app_name = 'coffeeshop'
urlpatterns = [

	url(r'^$', Product_list.as_view(), name='index'),
	url(r'^user/$', views.user_view, name='user'),
	url(r'^user/h1$', views.h1, name='h1'),
	url(r'^user/h2$', views.h2, name='h2'),
	url(r'^user/h3$', views.h3, name='h3'),
	url(r'^user/h4$', views.h4, name='h4'),	
	url(r'^register_sell/$', Sell_product.as_view(), name='register_sell'),
	url(r'^combos/$', views.combos_view, name='combos'),
	url(r'^products_list/$', product_table.as_view(), name='product_table'),
	url(r'^check_sells/$', views.view_check_product, name='check_sells'),
	url(r'^admin_register/client/$', Client_register.as_view(), name='client_register'),
	url(r'^add_product/$', Product_add.as_view(), name='add_products'),
	url(r'^admin_register/$', Client_table.as_view(), name='admin_register'),
	url(r'^product/(?P<product_id>[0-9]+)$', views.description_view, name ='product'),
	url(r'^admin_register/delete_client/(?P<pk>\d+)$', Client_delete.as_view(), name = 'delete_client'),	
	url(r'^products_list/delete_product/(?P<pk>\d+)$', Product_delete.as_view(), name = 'product_delete'),
	url(r'^admin_register/edit_client/(?P<pk>\d+)$', Client_edit.as_view(), name = 'client_edit')
]
