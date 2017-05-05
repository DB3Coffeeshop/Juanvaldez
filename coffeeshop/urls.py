from django.conf.urls import url

from . import views


app_name = 'coffeeshop'
urlpatterns = [

	url(r'^$', views.principal_view.as_view(), name='index'),

]
