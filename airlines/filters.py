from django import forms
from .models import Airline
import django_filters


class AirlineFilter(django_filters.FilterSet):

    starting_airport = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    destination_airport = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    airlines = django_filters.CharFilter(
    widget=forms.Select(choices=(('', 'Select Airlines'),) + Airline.AIRLINE_CHOICES, attrs={'class': 'form-control'}))

    # airlines = django_filters.CharFilter(
    #     widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Airline
        #fields = '__all__'
        fields = ['starting_airport', 'destination_airport', 'airlines']
