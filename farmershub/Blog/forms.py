from django import forms
from .models import *
class addblog(forms.ModelForm):
  class Meta:
    model=Blog
    fields='__all__'
