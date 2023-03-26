

from .models import Podik
from django import forms
from django.forms import TextInput, Select
from django.db.models import Q
import django_filters

class PodFilter(django_filters.FilterSet):
    categoryId = django_filters.ChoiceFilter(lookup_expr = "exact", choices = ((220,"Pod система"), (221, "Пристрої"), (239, "Одноразові"), (287, "ELF BAR"),(288, "HQD"), (222, "Картриджи"), (208, "Рідини для POD систем"), (236, "Українські сольові"), (237,"Сольові преміум")), widget = Select(attrs = {'class': 'catId_input'}))
    price = django_filters.RangeFilter(method="filter_pod_system")
    param = django_filters.MultipleChoiceFilter(lookup_expr = "exact",choices = Podik.objects.values_list('name', 'name'), widget=forms.CheckboxSelectMultiple(attrs = {'class': 'param_input invisible'}))
    class Meta:
        model = Podik
        fields = ({'price', 'categoryId', 'param'})
    def filter_pod_system(self, queryset, name, price1):
        print(price1)
        start = int(price1.start)
        stop = int(price1.stop)
        step = price1.step
        return queryset.filter(Q(price__gte = start)&Q(price__lte = stop))


