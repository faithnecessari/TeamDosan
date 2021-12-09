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

#hdasdhasdhasd


class FeedbackForm(forms.ModelForm):

    class Meta:
            model = Feedback
            fields= "__all__"

class ShopForm(forms.ModelForm):

    class Meta:
            model = Shops
            fields= "__all__"