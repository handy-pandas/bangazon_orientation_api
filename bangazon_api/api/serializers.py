from django.contrib.auth.models import User, Group
from rest_framework import serializers


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