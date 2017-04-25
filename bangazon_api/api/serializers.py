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
        exclude = ()


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
        exclude = ()


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class included in REST framework setup.

    Arguments:
    A hyperlink.

    Author: Talbot Lawrence
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''

        model = Customer
        exclude = ()


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
        exclude = ()


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
        exclude = ()


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
        exclude = ()

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose Order table to the API

    Arguments:
        A hyperlink.

    Author: Taylor perkins
    '''
    class Meta:
        model = Order
        exclude = ()


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


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose the employees to the API.

    Arguments:
    A hyperlink.
    Author: Talbot Lawrence
    '''
    class Meta:
        model = Employee
        exclude = ()


class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose Training Programs to the API

    Arguments: Title, StartDate, EndDate, Max

    Author: Aaron Barfoot
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''

        model = Training
        exclude = ()

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to expose the computers table to the API.

    Arguments:
    A hyperlink.

    Author: James Tonkin
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the computers model.
        '''
        model = Computer
        exclude = ()
