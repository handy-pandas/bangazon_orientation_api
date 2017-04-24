from django.db import models


<<<<<<< HEAD
class Product(models.Model):
	# CategoryId = models.ForeignKey(ProductType)
	# CustomerId = models.ForeignKey(Customer)
	Title = models.CharField(max_length=55)
	Description = models.CharField(max_length=150)
	Price = models.DecimalField(max_digits=6, decimal_places=2)


=======
class Customer(models.Model):
    """Class designed for creating customers within database

    Methods: 

    Author: [Talbot Lawrence]
    """
    FirstName = models.CharField(max_length=44)
    LastName = models.CharField(max_length=44)
    JoinDate = models.DateField(max_length=20)
    InactiveDate = models.DateField(max_length=20)
    Inactive = models.IntegerField(max_length=1)
>>>>>>> master
