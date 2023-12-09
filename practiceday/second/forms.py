from django import forms 
from .models import Modelform

class modelform(forms.ModelForm):
    class Meta:
        model = Modelform
        fields= "__all__"
