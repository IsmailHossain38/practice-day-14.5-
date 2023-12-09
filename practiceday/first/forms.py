from django import forms
from django.forms.widgets import NumberInput
import datetime


FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class AllForms(forms.Form):
    name = forms.CharField(max_length = 10)
    comment = forms.CharField(widget=forms.Textarea)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Please enter your email address", required = False)
    agree = forms.BooleanField(initial=True)
    date = forms.DateField(initial=datetime.date.today)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    first_name = forms.CharField(initial='ismail')
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
