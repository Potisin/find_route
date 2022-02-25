from django import forms

from cities.models import City


class HtmlForm(forms.Form):
    name = forms.CharField(label='Название города', max_length=100)


class CityForm(forms.ModelForm):
    name = forms.CharField(label='Название города', widget=forms.TextInput(attrs=
                                                                           {'class': 'form-control',
                                                                            'placeholder': 'Введите название города'}))

    class Meta:
        model = City
        fields = ('name',)
