from django.shortcuts import render ,redirect
from . import forms

# Create your views here.
def second(request):
    if request.method == 'POST':
        Model_form = forms.modelform(request.POST) 
        if Model_form.is_valid():  
            Model_form.save()  
            return redirect("second")
    else:
        Model_form = forms.modelform() 
        
    return render(request,'second.html' , {"Modelform": Model_form})