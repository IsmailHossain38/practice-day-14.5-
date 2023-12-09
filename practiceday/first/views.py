from django.shortcuts import render
from .forms import AllForms
# Create your views here.
def app(request):
    data = AllForms()
    return render(request,'./application/app.html' , {"data":data})