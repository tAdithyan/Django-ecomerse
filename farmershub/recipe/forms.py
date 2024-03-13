from django import forms
from .models import *
class addrecipes(forms.ModelForm):
  prep_time=forms.IntegerField(widget=forms.NumberInput(
    attrs={
      'placeholder':'prepration time',
      'class':'Discount'
    }
    
    
  ))
  cook_time=forms.IntegerField(widget=forms.NumberInput(
    attrs={
      'placeholder':'cooking time',
      'class':'Discount'
    }
    
    
  ))

  class Meta:
    model=Recipe
    fields='__all__'

