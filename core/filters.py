from django_filters import FilterSet
from .models import Order


class ContactFilter(FilterSet):
    class Meta:
        model = Order
        fields = ['name']