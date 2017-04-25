from django.db import models

class Order(models.Model):
    """This class defines what bangazon's Order table within the database will look like
        You need both PaymentType and Customer table for this to work correctly

<<<<<<< HEAD
    Attributes:
        PaymentTypeId (INT): Payment Type Id referencing Payment Type table (FK)
        CustomerId (INT): Customer Id referencing Customer table (FK)
    """
    PaymentTypeId = models.ForeignKey(PaymentType)    
    CustomerId = models.ForeignKey(Customer)        
=======
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
>>>>>>> bda9b69bbe3aa3b63eb9b3bd20455d91e547ec09

class ProductOrder(models.Model):
    """This class is a join table for both the Product and Order Table within Bangazon db
        You will need both the Product and Order tables created for this table to apply

<<<<<<< HEAD
    Attributes:
        ProductId (INT): Product Id referencing Product table (FK)
        OrderId (INT): Order Id referencing Order table (FK)
    """
    ProductId = models.ForeignKey(Product)    
    OrderId = models.ForeignKey(Order)        
=======
class Product(models.Model):
	# CategoryId = models.ForeignKey(ProductType)
	# CustomerId = models.ForeignKey(Customer)
	Title = models.CharField(max_length=55)
	Description = models.CharField(max_length=150)
	Price = models.DecimalField(max_digits=6, decimal_places=2)
>>>>>>> bda9b69bbe3aa3b63eb9b3bd20455d91e547ec09

