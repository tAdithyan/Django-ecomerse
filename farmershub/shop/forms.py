from django import forms
from .models import *
class additeam(forms.ModelForm):
  class Meta:
    model=Product
    fields='__all__'

class addcategory(forms.ModelForm):
  class Meta:
    model=Category
    fields='__all__'
