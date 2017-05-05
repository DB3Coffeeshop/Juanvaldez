from django.contrib import admin
from .models import *

admin.site.register(departament)
admin.site.register(city)
admin.site.register(provider)
admin.site.register(client)
admin.site.register(description_bill_payment)
admin.site.register(bill_payment)
admin.site.register(product_type)
admin.site.register(product)
admin.site.register(sale)

