from django.db import models


class PaymentType(models.Model):
    '''
    A class that adds a PaymentType table to the database.

class Customer(models.Model):
    """Class designed for creating customers within database


    Arguments:
    A model provided by django framework.

    Author:
    wocaldwell
    '''
    AccountNumber = models.IntegerField(max_length=99)
    Name = models.CharField(max_length=255)
    # CustomerId = models.ForeignKey(CustomerId)
    CustomerId = models.CharField(max_length=99)


    Author: [Talbot Lawrence]
    """
    FirstName = models.CharField(max_length=44)
    LastName = models.CharField(max_length=44)
    JoinDate = models.DateField(max_length=20)
    InactiveDate = models.DateField(max_length=20)
    Inactive = models.IntegerField(max_length=1)


class Product(models.Model):
	# CategoryId = models.ForeignKey(ProductType)
	# CustomerId = models.ForeignKey(Customer)
	Title = models.CharField(max_length=55)
	Description = models.CharField(max_length=150)
	Price = models.DecimalField(max_digits=6, decimal_places=2)

