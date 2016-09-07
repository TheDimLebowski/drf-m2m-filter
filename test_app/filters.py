import django_filters
from models import User, Label

class UserFilter(django_filters.FilterSet):
    labels = django_filters.filters.BaseInFilter(
        name='labels',
        lookup_type='in',
    )

    class Meta:
        model = User
        fields = ('labels',)
