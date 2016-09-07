from django.shortcuts import render
from models import User
from serializers import UserSerializer
from rest_framework import viewsets, filters
from filters import UserFilter

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = UserFilter
    filter_fields = ('labels',)
