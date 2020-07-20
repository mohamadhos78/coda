from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import emailservice



class contact_us(TemplateView):
    users = []
    user_query = UserProfile.objects.all()
    for a in user_query:
        users.append({
        'name':a.user.first_name+' '+a.user.last_name ,
        'img':a.avatar.url ,
        'description':a.description , 
        'theory':a.theory ,
        })
    def get(self, request, **kwargs):
        context ={
            'users':self.users ,
        }
        return render(request,"contact.htm", context)
class index(TemplateView):
    users = []
    posts = []
    user_query = UserProfile.objects.all()
    post_query = Article.objects.filter(promote=True)
    for a in user_query:
        users.append({
        'name':a.user.first_name+' '+a.user.last_name ,
        'img':a.avatar.url ,
        'description':a.description , 
        'theory':a.theory ,
        })
    for b in post_query:
        posts.append({
        'author':b.author ,
        'cover':b.cover.url ,
        'content':b.content , 
        'category':b.category,
        'title':b.title ,
        })     
    def get(self, request, **kwargs):
        if request.method == "POST":
            filled_form = emailservice(request.POST)
            if filled_form.is_valid():
                filled_form.save()
            else:
                form = emailservice()
            context = {
                'form' : form  ,
            }
            return render(request , 'index.htm'  ,context)
        else:   
            form = emailservice()
            context ={
                'users':self.users ,
                'posts':self.posts ,
                'form': form ,
            }
            return render(request,"index.htm", context)

    def post(self, request, **kwargs):
        form = emailservice()
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        else:
            form = emailservice()
        form = emailservice()
        context ={
            'users':self.users ,
            'posts':self.posts ,
            'form': form
        }
        return render(request,"index.htm", context)

class costs(TemplateView):
    def get(self, request, **kwargs):
        context = {
        }
        return render(request , 'costs.htm' , context)
class portfolio(TemplateView):
    def get(self, request, **kwargs):
        context ={
        }
        return render(request,"portfolio.htm", context)
