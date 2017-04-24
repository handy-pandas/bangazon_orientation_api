from django.db import models

class Order(models.Model):
    """This class defines what bangazon's Order table within the database will look like
        You need both PaymentType and Customer table for this to work correctly

    Attributes:
        PaymentTypeId (INT): Payment Type Id referencing Payment Type table (FK)
        CustomerId (INT): Customer Id referencing Customer table (FK)
    """
    PaymentTypeId = models.ForeignKey(PaymentType)    
    CustomerId = models.ForeignKey(Customer)        

class ProductOrder(models.Model):
    """This class is a join table for both the Product and Order Table within Bangazon db
        You will need both the Product and Order tables created for this table to apply

    Attributes:
        ProductId (INT): Product Id referencing Product table (FK)
        OrderId (INT): Order Id referencing Order table (FK)
    """
    ProductId = models.ForeignKey(Product)    
    OrderId = models.ForeignKey(Order)        

