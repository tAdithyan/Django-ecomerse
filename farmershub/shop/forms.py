from django import forms
from .models import *
class additeam(forms.ModelForm):
  class Meta:
    model=Product
    fields='__all__'