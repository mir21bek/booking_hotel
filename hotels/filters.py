import django_filters

from .models import ApartmentType


class PriceFilter(django_filters.FilterSet):
    price_gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter('name', lookup_expr='icontains')

    class Meta:
        model = ApartmentType
        fields = ('price_gte', 'price_lte', 'name',)
