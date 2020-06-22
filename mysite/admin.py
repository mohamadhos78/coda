from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title' , 'descrption']
    list_display = ['title' , 'category' , 'author']

admin.site.register(Article , ArticleAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'avatar']
    
admin.site.register(UserProfile , UserProfileAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'cover']

admin.site.register(Category , CategoryAdmin)
class emailservicemodelAdmin(admin.ModelAdmin):
    list_display = ['email','name','family']
    
admin.site.register(emailservicemodel , emailservicemodelAdmin)

admin.site.register(Skill)
