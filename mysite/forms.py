from django import forms
from .models import emailservicemodel , contact_us

class emailservice(forms.ModelForm):
    class Meta:
        model = emailservicemodel
        fields = ['name','family','email']
        labels = { 'name' :'name'  , 'family' : 'family'  ,  'email' :'email'}
class contact_us_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields =['name','phone','email','text']
        labels = { 
            'name' :'name'   ,
            'phone' : 'phone',  
            'email' :'email' ,
            'text':'text'    ,
            }
