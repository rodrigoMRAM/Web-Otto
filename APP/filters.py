import django_filters
from APP.models import Clientes

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Clientes
        fields = {'nombre':['contains'],'patente':['contains'], "mes":["contains"]}