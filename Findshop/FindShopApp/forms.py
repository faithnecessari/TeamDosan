from django import forms
from .models import *

class FindShopAppForm(forms.ModelForm):
    class Meta:
            model = Customer
            fields= "__all__"

class AdminForm(forms.ModelForm):
         
    class Meta:
            model = Admin
            fields= "__all__"
