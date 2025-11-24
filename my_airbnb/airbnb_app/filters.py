from django_filters import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'property_type': ['exact'],
            'city': ['exact'],
            'price_per_night': ['gt', 'lt'],
            'property_stars': ['exact']
        }