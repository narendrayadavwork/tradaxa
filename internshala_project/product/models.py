from django.db import models
import datetime

# Create your models here.

class ProductData(models.Model):
	name = models.CharField(max_length=150, default="aaa")
	weight = models.CharField(max_length=100, default="4")
	price = models.CharField(max_length=6)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'productdbs'
		app_label = 'product'

	# class Meta:
	# 	app_label = 'product_data'

	def __str__(self):
		return self.name


	# class meta:
	# 	table_db =