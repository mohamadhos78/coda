from django import forms
from .models import emailservicemodel, Comment
from .models import contact_us, centure


class emailservice(forms.ModelForm):
    class Meta:
        model = emailservicemodel
        fields = ['name','family','email']
        labels = { 'name' :'name'  , 'family' : 'family'  ,  'email' :'email'}


class contact_us_form(forms.ModelForm):
    class Meta:
        model = contact_us
        fields = ['name', 'phone', 'email', 'text']
        labels = { 
            'name': 'name',
            'phone': 'phone',
            'email': 'email',
            'text': 'text',
            }


class centure_form(forms.ModelForm):
    class Meta:
        model = centure
        fields =['centure_name', 'centure_phone', 'centure_email', 'centure_description']
        labels = { 
            'centure_name': 'centure_name',
            'centure_phone': 'centure_phone',
            'centure_email': 'centure_email',
            'centure_description': 'centure_description',
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "name", "email"]
