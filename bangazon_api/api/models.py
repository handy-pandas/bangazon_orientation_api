from django.db import models


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
    # CustomerId = models.ForeignKey(CustomerId)
    CustomerId = models.CharField(max_length=99)