from django.conf.urls import url, include
from test_app.models import User
from test_app.views import UserViewSet
from rest_framework import routers

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
