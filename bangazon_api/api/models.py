from django.db import models


class Customer(models.Model):
    """Class designed for creating customers within database
    Methods:
    Author: Talbot Lawrence
    """
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    join_date = models.DateField(max_length=20)
    inactive_date = models.DateField(max_length=20)
    inactive = models.IntegerField()

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
    account_number = models.IntegerField()
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer)


class Product(models.Model):
    """Class for adding product table to the database
    Methods:

    Author: Aaron Barfoot

    """
    product_type = models.ForeignKey(ProductType)
    customer = models.ForeignKey(Customer)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Order(models.Model):
    """This class defines what bangazon's Order table within the database will look like
        You need both PaymentType and Customer table for this to work correctly
    Attributes:
        payment_type (INT): Payment Type Id referencing Payment Type table (FK)
        customer (INT): Customer Id referencing Customer table (FK)
    Author: Taylor Perkins
    """
    payment_type = models.ForeignKey(PaymentType)
    customer = models.ForeignKey(Customer)

class ProductOrder(models.Model):
    """This class is a join table for both the Product and Order Table within Bangazon db
        You will need both the Product and Order tables created for this table to apply
    Attributes:
        product (INT): Product Id referencing Product table (FK)
        order (INT): Order Id referencing Order table (FK)
    Author: Taylor Perkins
    """

    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)


class Department(models.Model):
    """
    Class for adding product table to the database


    name = models.CharField(max_length=55)
    budget = models.DecimalField(max_digits=6, decimal_places=2)

    Author:
    wocaldwell
    """
    name = models.CharField(max_length=55)
    budget = models.DecimalField(max_digits=6, decimal_places=2)

class Employee(models.Model):
    """Class designed for creating employees within database

    Attributes:
    department (INT): Department Id referencing the Department table (FK)

    Author: Talbot Lawrence
    """
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    title = models.CharField(max_length=44)
    department = models.ForeignKey(Department)


class Training(models.Model):
	"""Class for adding training program to the database

	Methods:

	Author: Aaron Barfoot
	"""
	title = models.CharField(max_length=55)
	start_date = models.DateField(max_length=10)
	end_date = models.DateField(max_length=10)
	max_attendance = models.IntegerField()


class EmployeeTraining(models.Model):
    """This class is a join table for both the Employee and Training Table within Bangazon db
        You will need both the Employee and Training tables created for this table to apply

    Attributes:
        employee (INT): Employee Id referencing Employee table (FK)
        training (INT): Training Id referencing Training table (FK)

    Author: Aaron Barfoot
    """
    employee = models.ForeignKey(Employee)
    training = models.ForeignKey(Training)


class Computer(models.Model):
    """ Class to expose the computers to the API.

    Author: James Tonkin
    """
    employee = models.ForeignKey(Employee)
    purchase_date = models.DateField(max_length=20)
    decom_date = models.DateField(max_length=20)
