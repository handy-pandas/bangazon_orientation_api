from django.db import models

# Create your models here.


class Customer(models.Model):
    """Class designed for creating customers within database

    Methods:

    Author: [Talbot Lawrence]
    """
    FirstName = models.CharField(max_length=44)
    LastName = models.CharField(max_length=44)
    JoinDate = models.DateField(max_length=20)
    InactiveDate = models.DateField(max_length=20)
    Inactive = models.IntegerField()

class ProductType(models.Model):
    """ Class to expose the product types to the API.

    Author: James Tonkin
    """
    name = models.CharField(max_length=255)



class PaymentType(models.Model):
    '''
    A class that adds a PaymentType table to the database.

    Arguments:
    A model provided by django framework.

    Author:
    wocaldwell
    '''
    AccountNumber = models.IntegerField()
    Name = models.CharField(max_length=255)
    CustomerId = models.ForeignKey(Customer)

    
class Product(models.Model):
	"""Class for adding product table to the database

	Methods:

	Author: Aaron Barfoot
	"""
	CategoryId = models.ForeignKey(ProductType)
	CustomerId = models.ForeignKey(Customer)
	Title = models.CharField(max_length=55)
	Description = models.CharField(max_length=150)
	Price = models.DecimalField(max_digits=6, decimal_places=2) 



class Training(models.Model):
	"""Class for adding training program to the database

	Methods:

	Author: Aaron Barfoot
	"""
	Title = models.CharField(max_length=55)
	StartDate = models.DateField(max_length=10)
	EndDate = models.DateField(max_length=10)
	Max = models.IntegerField(max_length=5)









