from django.conf.urls import url

from . import views


app_name = 'coffeeshop'
urlpatterns = [

	url(r'^$', views.principal_view, name='index'),
	url(r'^user/$', views.user_view, name='user'),
	url(r'^user/h1$', views.h1, name='h1'),
	url(r'^user/h2$', views.h2, name='h2'),
	url(r'^user/h3$', views.h3, name='h3'),
	url(r'^user/h4$', views.h4, name='h4'),	
	url(r'^register_sell/$', views.view_register_sell, name='register_sell'),
	url(r'^prom_comb/$', views.promotions_combos_view, name='prom_comb'),
	url(r'^check_sells/$', views.view_check_product, name='check_sells'),
	url(r'^add_product/$', views.product_add_view, name='add_products'),
	url(r'^admin_register/$', views.view_register_admin, name='admin_register'),
	url(r'^product/(?P<product_id>[0-9]+)$', views.description_view, name ='product'),
]
