from django.contrib.auth.models import *
from rest_framework import viewsets
from bangazon_api.api.models import *
from bangazon_api.api.serializers import *

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
    API endpoint that allows product types to be viewed or edited.

    Author: James Tonkin
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product types to be viewed or edited.

    Author:
    wocaldwell
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.

    Author: Aaron Barfoot
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.

    Author: Taylor Perkins
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.

    Author:
    wocaldwell
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Create Model to be viewed or edited.

    Author:
    Talbot Lawrence
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TrainingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows training progeams to be viewed or edited.
    Author: Aaron Barfoot
    """
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    

class ComputerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows computers to be viewed or edited.

    Author: James Tonkin
    """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
