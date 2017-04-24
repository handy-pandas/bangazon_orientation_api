from django.db import models

# Create your models here.
class Product(models.Model):
	"""Class for adding product table to the database

	Methods:

	Author: [Aaron Barfoot]
	"""
	# CategoryId = models.ForeignKey(ProductType)
	# CustomerId = models.ForeignKey(Customer)
	Title = models.CharField(max_length=55)
	Description = models.CharField(max_length=150)
	Price = models.DecimalField(max_digits=6, decimal_places=2)
