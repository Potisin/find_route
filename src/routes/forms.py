from django import forms
from django.forms import SelectMultiple

from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label='Откуда', queryset=City.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control js-example-basic-single'
        }))

    to_city = forms.ModelChoiceField(
        label='Куда', queryset=City.objects.all(), widget=forms.Select(attrs={
            'class': 'form-control js-example-basic-single'
        }))

    total_travel_time = forms.IntegerField(label='Время в пути', widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Время в пути'}))

    cities = forms.ModelMultipleChoiceField(label='Через города', queryset=City.objects.all(),
                                            required=False, widget=SelectMultiple(
            attrs={'class': 'form-control js-example-basic-multiple'}))


class RouteModelForm(forms.ModelForm):
    name = forms.CharField(label='Название маршрута', max_length=255,
                           widget=forms.TextInput(attrs=
                                                  {'class': 'form-control',
                                                   'placeholder': 'Введите название маршрута'}))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())

    to_city = forms.ModelChoiceField(queryset=City.objects.all(), widget=forms.HiddenInput())

    total_travel_time = forms.IntegerField(widget=forms.HiddenInput())

    trains = forms.ModelMultipleChoiceField(queryset=Train.objects.all(),
                                            required=False, widget=SelectMultiple(
            attrs={'class': 'form-control d-none'}))

    class Meta:
        model = Route
        fields = '__all__'
