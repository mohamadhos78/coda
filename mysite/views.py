from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import emailservice



class contactpage(TemplateView):
    template_name = "Landing.htm"

class index(TemplateView):
    def get(self , request , **kwargs):
        form = emailservice()
        
        article_data=[]
        all_article=Article.objects.all()[:9]
        for article in all_article:
            article_data.append({
                'title': article.title , 
                'created_at' :article.created_at.date ,
                'cover' : article.cover.url ,
                'category' : article.category ,
            })
        promoted_post = []
        all_promote = Article.objects.filter(promote=True)
        for promoted in all_promote:
            promoted_post.append({
                'promoted_title' : promoted.title , 
                'promoted_author' :promoted.author.user.first_name +' '+promoted.author.user.last_name  ,
                'promoted_cover' :promoted.cover.url if promoted.cover else None,
                'promoted_category' : promoted.category.title ,
                'promoted_created_at' :promoted.created_at.date ,
                'promoted_avatar' :promoted.author.avatar.url if promoted.author.avatar else None ,
            })
        context = {
            'article_data' : article_data , 
            'promoted_post' : promoted_post ,
            'form':form , 
        }
        return render(request , 'index.html' , context)


def signup(request):
    member_skill = Skill.objects.all()
    skills=[]
    for skill in member_skill:
        skills.append({
                'skill_objects' :skill.title ,
        })
    if request.method == "POST":
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note =" Dear {} you subscribed successfully".format(filled_form.cleaned_data['name'] )
        else:
            note = "sorry you didn't registered"
        form = emailservice()
        context = {
            'form' : form  ,
            'note' : note  ,
            'skills':skills,
        }
        return render(request , 'Form.htm'  ,context)
    else:
        # member_skill = Skill.objects.all()
        # skills=[]
        # for skill in member_skill:
        #     skills.append({
        #         'skill_objects' :skill.title ,
        #     })
            
        form = emailservice()
        note = 'welcome to signup page '
        return render(request , 'Form.htm' , {'form': form , 'note':note ,'skills':skills})