from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import emailservice ,centure_form


class contact_us(TemplateView):
    users = []
    user_query = adminProfile.objects.all()
    for a in user_query:
        users.append({
        'name':a.user.first_name+' '+a.user.last_name ,
        'img':a.avatar.url ,
        'description':a.description , 
        'theory':a.theory ,
        })
    centure_form = centure_form()
    form = emailservice()
    def get(self, request, **kwargs):
        context ={
            'users':self.users ,
            # 'mains':self.mains ,
            'centure':self.centure_form ,
            'form':self.form ,
        }
        return render(request,"contact.htm", context)
    def post(self, request, **kwargs):
        centure_filled_form = centure_form(request.POST)
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        if centure_filled_form.is_valid():
            centure_filled_form.save()
        context ={
            'users':self.users ,
            #'main':self.mains ,
            'form': self.form ,
            'centure_form':self.centure_form ,
        }
        return render(request,"index.htm", context)
class index(TemplateView):
    mains = []
    users = []
    posts = []
    user_query = adminProfile.objects.all()
    post_query = Article.objects.filter(promote=True)
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo':c.logo.url ,
            'field1':c.field1 ,
            'field2':c.field2 ,
            'field3':c.field3 ,
            'field4':c.field4 ,
        })
    for a in user_query:
        users.append({
        'name':a.user.first_name+' '+a.user.last_name ,
        'img':a.avatar.url ,
        'description':a.description , 
        'theory':a.theory ,
        'github':a.social_media.github ,
        'linkedin':a.social_media.linkedin ,
        'twitter':a.social_media.twitter ,
        'telegram':a.social_media.telegram ,
        'bale':a.social_media.bale ,
        'instagram':a.social_media.instagram ,
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
        form = emailservice()
        context ={
            'users':self.users ,
            'posts':self.posts ,
            'main':self.mains ,
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
            'main':self.mains ,
            'form': form
        }
        return render(request,"index.htm", context)

class costs(TemplateView):
    def get(self, request, **kwargs):
        # mains = []
        # main_query = main.objects.all()
        # for c in main_query:
        #     mains.append({
        #         'logo':c.logo ,
        #         'field1':c.field1 ,
        #         'field2':c.field2 ,
        #         'field3':c.field3 ,
        #         'field4':c.field4 ,
        #     })
        context = {
            # 'main':self.mains ,
        }        
        return render(request , 'costs.htm' , context)
class portfolio(TemplateView):
    def get(self, request, **kwargs):
        #mains = []
        #main_query = main.objects.all()
        #for c in main_query:
        #    mains.append({
        #        'logo':c.logo ,
        #        'field1':c.field1 ,
        #        'field2':c.field2 ,
        #        'field3':c.field3 ,
        #        'field4':c.field4 ,
        #    })
        context ={
        #    'main':self.mains ,
        }
        return render(request,"portfolio.htm", context)

