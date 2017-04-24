from django.contrib.auth.models import *
from rest_framework import viewsets
from bangazon_api.api.serializers import *
from bangazon_api.api.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Create Model to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Create Model to be viewed or edited.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
