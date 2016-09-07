import django_filters
from models import User, Label

class UserFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all())

    class Meta:
        model = User
        fields = ('labels',)
