from django.contrib.auth.models import *
from rest_framework import serializers

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

    Arguments: FirstName, LastName, JoinDate, InactiveDate, Inactive

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
    Author:
    wocaldwell
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''
        model = PaymentType
        fields = ('url', 'Name', 'AccountNumber', 'CustomerId')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose Product table to the API

    Arguments: CategoryId, CustomerId, Title, Description, Price

    Author: Aaron Barfoot
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''
        model = Product
        fields = ('CategoryId', 'CustomerId', 'Title', 'Description', 'Price')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose Order table to the API

    Arguments:
        A hyperlink.

    Author: Taylor perkins
    '''
    class Meta:
        model = Order
        fields = ('url', 'PaymentTypeId', 'CustomerId')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose department table to the API.

    Author:
    wocaldwell
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''

        model = Department
        exclude = ()



