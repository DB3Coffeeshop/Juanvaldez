from django.conf.urls import url

from . import views


app_name = 'coffeeshop'
urlpatterns = [

	url(r'^$', views.principal_view, name='index'),
	url(r'^user/$', views.admin_view, name='user'),
	url(r'^user/h1$', views.h1, name='h1'),
	url(r'^user/h2$', views.h2, name='h2'),
	url(r'^user/h3$', views.h3, name='h3'),
	url(r'^user/h4$', views.h4, name='h4'),
	url(r'^administrador$', views.view_x, name='x'),
	url(r'^product/(?P<product_id>[0-9]+)$', views.description_view, name ='product'),
]
