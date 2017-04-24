from django.contrib.auth.models import User, Group
from rest_framework import serializers
from bangazon_api.api.api_database_management.user_interface.create_models import *


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

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Class to serialize a payment type table in the API.

    Arguments:
    A hyperlink.
    '''
    class Meta:
        '''
        Defines what fields are exposed to the api from the model.
        '''
        model = PaymentType
        fields = ('url', 'Name', 'AccountNumber', 'CustomerId')

