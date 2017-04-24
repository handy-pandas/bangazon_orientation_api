from django.db import models


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
