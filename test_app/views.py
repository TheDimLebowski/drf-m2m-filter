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
    def get_queryset(self):
        queryset = User.objects.all()
        labels = eval(self.request.query_params.get('labels', []))
        for label in labels:
            queryset = queryset.filter(labels__in=[label])
        return queryset
