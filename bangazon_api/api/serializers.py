from django.contrib.auth.models import *
from rest_framework import serializers
from django.db import models
from bangazon_api.api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class included in REST framework setup.

    Arguments:
    A hyperlink.
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class included in REST framework setup.

    Arguments:
    A hyperlink.
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''
        model = Group
        fields = ('url', 'name')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class included in REST framework setup.
    Author: [Talbot Lawrence]

    Arguments: 
    A hyperlink.
    '''

    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''

        model = Customer
        fields = ('FirstName', 'LastName', 'JoinDate', 'InactiveDate', 'Inactive')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose the ProductType table to the API.

    Arguments:
    A hyperlink.

    Author: James Tonkin
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the ProductType model.
        '''
        model = ProductType
        fields = ('url', 'name')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to serialize a payment type table in the API.

    Arguments:
    A hyperlink.

    Autor:
    wocaldwell
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''

        model = PaymentType
        fields = ('url', 'Name', 'AccountNumber', 'CustomerId')
