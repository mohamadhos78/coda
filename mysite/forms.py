from django import forms
from .models import emailservicemodel

class emailservice(forms.ModelForm):
    class Meta:
        model = emailservicemodel
        fields = ['name','family','email','skill']
        labels = { 'name' :'name'  , 'family' : 'family'  ,  'email' :'email','skill':'skill'}
