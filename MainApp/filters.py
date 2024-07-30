from django_filters import rest_framework as filters
from .models import *


class CarFilters(filters.FilterSet):
    marka = filters.ChoiceFilter(field_name='marka__marka', choices=Marka.objects.all().values_list('marka', 'marka').distinct())
    body = filters.ChoiceFilter(field_name='body__body', choices=Body.objects.all().values_list('body', 'body').distinct())
    body_color = filters.ChoiceFilter(field_name='body_color__body_color', choices=BodyColor.objects.all().values_list('body_color', 'body_color').distinct())
    steering_wheel = filters.ChoiceFilter(field_name='steering_wheel__steering_wheel', choices=StreengWhell.objects.all().values_list('steering_wheel', 'steering_wheel').distinct())
    lte_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    gte_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    year_lte = filters.ChoiceFilter(field_name='year_of_manufacture__year_of_manufacture', choices=Year.objects.all().values_list('year_of_manufacture', 'year_of_manufacture').distinct(), lookup_expr='lte')
    year_gte = filters.ChoiceFilter(field_name='year_of_manufacture__year_of_manufacture', choices=Year.objects.all().values_list('year_of_manufacture', 'year_of_manufacture').distinct(), lookup_expr='gte')
    mileage_lte = filters.NumberFilter(field_name='mileage', lookup_expr='lte')
    mileage_gte = filters.NumberFilter(field_name='mileage', lookup_expr='gte')
    checkpoint = filters.ChoiceFilter(field_name='checkpoint__checkpoint', choices=Checkpoint.objects.all().values_list('checkpoint', 'checkpoint').distinct())
    drive_unit = filters.ChoiceFilter(field_name='drive_unit__drive_unit', choices=DriveUnit.objects.all().values_list('drive_unit', 'drive_unit').distinct())
    owners_lte = filters.NumberFilter(field_name='owners', lookup_expr='lte')
    owners_gte = filters.NumberFilter(field_name='owners', lookup_expr='gte')

    class Meta:
        model = Car
        fields = ['marka', 'body', 'body_color', 'steering_wheel', 'lte_price', 'gte_price', 'year_lte', 'year_gte', 'mileage_lte', 'mileage_gte', 'checkpoint', 'drive_unit', 'owners']
