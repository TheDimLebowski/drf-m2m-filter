from models import User, Label
from filters import UserFilter
from rest_framework import serializers

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ('id','name')

class UserSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many = True)
    class Meta:
        model = User
        fields = ('id','labels')
