from django.conf.urls import url, include
from rest_framework import routers
from bangazon_api.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'producttype', views.ProductTypeViewSet)
router.register(r'paymenttype', views.PaymentTypeViewSet)
router.register(r'product', views.ProductViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^bangazon/api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
