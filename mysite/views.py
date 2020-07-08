from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import emailservice



class contact_us(TemplateView):
    template_name = "contact.htm"

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
