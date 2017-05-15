from django.db import models
from django.utils import timezone

class Departament(models.Model):
	id_dpto = models.IntegerField(primary_key = True)
	dpto_name = models.CharField(max_length=30, unique = True)

	
	def __str__(self):
		return self.dpto_name


class City(models.Model):
	id_city = models.IntegerField(primary_key = True)
	city_name = models.CharField(max_length=30, unique = True)
	id_dpto = models.ForeignKey(Departament, on_delete = models.CASCADE)


	def __str__(self):
		return self.city_name


class Provider(models.Model):
	id_provider = models.IntegerField(primary_key = True)
	provider_name = models.CharField(max_length = 30)
	tel_provider = models.IntegerField(unique = True)
	id_city = models.ForeignKey(City, on_delete = models.CASCADE)


	def __str__(self):
		return self.provider_name


class Client(models.Model):
	name_client = models.CharField(max_length=20)
	id_client = models.IntegerField(primary_key = True)
	id_city = models.ForeignKey(City, on_delete = models.CASCADE)
	points = models.IntegerField(default=0)


	def __str__(self):
		return self.name_client


class Description_bill_payment(models.Model):
	payment_modes = {
			('CC', 'Credit Card'),
			('CM', 'Cash Money'),
			}

	id_payment = models.IntegerField(default=0)
	pay_mode = models.CharField(max_length = 2, choices = payment_modes, default = 'CM')
	employee_name = models.CharField(max_length=20)


	def __str__(self):
		return str(self.id_payment)


class Bill_payment(models.Model):
	id_bill_payment = models.IntegerField(primary_key = True)
	id_client = models.ForeignKey(Client, on_delete = models.CASCADE)
	id_payment = models.ForeignKey(Description_bill_payment, on_delete = models.CASCADE)
	payment_date = models.DateTimeField()
	

	def __str__(self):
		return str(self.id_bill_payment)



class Promotion(models.Model):
	id_promotion = models.IntegerField(primary_key = True)
	percent_promotion = models.IntegerField(default=0)

	def __str__(self):
		return str(self.id_promotion)


class Product_type(models.Model):
	id_product_type = models.IntegerField(primary_key = True)
	product_type = models.CharField(max_length = 30, unique = True)
	product_description = models.TextField(max_length = 50)
	id_promotion = models.ForeignKey(Promotion, on_delete = models.CASCADE)
	
	def __str__(self):
		return str(self.id_product_type)



class Product(models.Model):
	id_product = models.IntegerField(primary_key = True)
	name_product = models.CharField(max_length = 20, unique = True)
	price = models.DecimalField(max_digits = 8, decimal_places = 3)
	stock = models.IntegerField(default=0)
	id_provider = models.ForeignKey(Provider, on_delete = models.CASCADE)
	id_product_type = models.ForeignKey(Product_type, null = True, blank = True)
	img_product = models.CharField(max_length = 30, unique = True, null = True)  #Puts here the img rute on our proyect
	id_promotion = models.ForeignKey(Promotion, on_delete = models.CASCADE, null = True)


	def __str__(self):
		return self.name_product



class Combo(models.Model):
	id_combo = models.IntegerField(primary_key = True)
	id_product = models.ForeignKey(Product, on_delete = models.CASCADE)
	combo_name = models.CharField(max_length = 30)
	price = models.DecimalField(max_digits = 8, decimal_places = 3)
	quantity_products = models.IntegerField(default = 0)

	def __str__(self):
		return self.combo_name



class Sale(models.Model):
	id_sale = models.IntegerField(primary_key = True)
	id_bill_payment = models.ForeignKey(Bill_payment, on_delete = models.CASCADE)
	quantity_sold = models.IntegerField()
	id_product = models.ForeignKey(Product, on_delete = models.CASCADE)
	sale_value = models.DecimalField(max_digits = 8, decimal_places = 3)


	def __str__(self):
		return str(self.id_sale)
