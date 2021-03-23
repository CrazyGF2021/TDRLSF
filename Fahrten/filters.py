import django_filters
from Fahrten.models import Fahrten

class FahrtenDatumFilter(django_filters.FilterSet):
    class Meta:
        model = Fahrten
        fields = ['gueltig_ab', 'gueltig_bis',]