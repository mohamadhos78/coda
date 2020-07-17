from django.conf.urls import url , include
from . import views


urlpatterns = [
    url(r"^$" , views.index.as_view() , name = 'index'),
    url(r'costs/$' , views.costs.as_view() , name = 'costs') ,
    url(r'contact_us/$' , views.contact_us.as_view() , name = 'contact_us') , 
]
