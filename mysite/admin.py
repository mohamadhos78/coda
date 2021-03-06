from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title' , 'descrption']
    list_display = ['title' , 'category' , 'author']

admin.site.register(Article , ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'cover']

admin.site.register(Category , CategoryAdmin)
class emailservicemodelAdmin(admin.ModelAdmin):
    list_display = ['email','name','family']


admin.site.register(emailservicemodel , emailservicemodelAdmin)

class contact_usAdmin(admin.ModelAdmin):
    search_fields = ['name' , 'email','text']
    list_display = ['name' , 'email' , 'phone']

admin.site.register(contact_us , contact_usAdmin)

admin.site.register(social_media)
class adminProfileAdmin(admin.ModelAdmin):
    list_display = ['user' , 'avatar']
admin.site.register(adminProfile , adminProfileAdmin)

admin.site.register(main)

admin.site.register(centure)
admin.site.register(Comment)