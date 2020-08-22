from django.conf.urls import url , include 
from django.urls import path
from . import views


urlpatterns = [
    url(r"^$", views.index.as_view(), name='index'),
    url(r'costs/$', views.costs.as_view(), name='costs'),
    url(r'contact_us/$', views.contact_us.as_view(), name='contact_us'),
    url(r'portfolio/$', views.portfolio.as_view(), name='portfolio'),
    url(r'blog/$', views.blog.as_view(), name='blog'),
    path('posts/<int:pk>/', views.posts, name='posts'),
]
