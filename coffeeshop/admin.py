from django.contrib import admin
from .models import *


class ProductInline(admin.TabularInline):
	model = Product


class Product_type_admin(admin.ModelAdmin):
	inlines = [
			ProductInline,
		]

admin.site.register(Departament)
admin.site.register(City)
admin.site.register(Provider)
admin.site.register(Client)
admin.site.register(Description_bill_payment)
admin.site.register(Bill_payment)
#admin.site.register(Product_type)
admin.site.register(Product_type, Product_type_admin)
admin.site.register(Sale)
admin.site.register(Promotion)
admin.site.register(Combo)
