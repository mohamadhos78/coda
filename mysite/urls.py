from django.conf.urls import url , include
from . import views


urlpatterns = [
    url(r"^$" , views.index.as_view() , name = 'index'),
    url(r'signup/$' , views.signup , name = 'signup') , 
    url(r'contactpage/$' , views.contactpage.as_view() , name = 'contact') , 
]
