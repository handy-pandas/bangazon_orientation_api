from django.db import models

class Order(models.Model):
    """This class defines what bangazon's Order table within the database will look like

    Attributes:
        PaymentTypeId (INT): Payment Type Id referencing table (FK)
        CustomerId (INT): Customer Id referencing table (FK)
    """
    PaymentTypeId = models.ForeignKey(PaymentTypes)    
    CustomerId = models.ForeignKey(Customers)    



