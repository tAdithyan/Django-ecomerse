from django import forms
from .models import *
class additeam(forms.ModelForm):
  Discount=forms.IntegerField(widget=forms.NumberInput(
    attrs={
      'placeholder':'Discount',
      'class':'Discount'
    }
    
    
  ))
  Currentprice=forms.IntegerField(widget=forms.NumberInput(
    attrs={
      'placeholder':'Discount',
      'class':'Discount'
    }
    
    
  ))
  Oldprice=forms.IntegerField(widget=forms.NumberInput(
    attrs={
      'placeholder':'Discount',
      'class':'Discount'
    }
    
    
  ))
  class Meta:
    model=Product
    fields='__all__'

class addcategory(forms.ModelForm):
  class Meta:
    model=Category
    fields='__all__'
