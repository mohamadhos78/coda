from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
from phone_field import PhoneField

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg','jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='user_avatar/', null=False, blank=False, validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)
    theory  = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='article_cover/', null=False, blank=False, validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateTimeField(auto_now = True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='category_cover/', null=False, blank=False, validators=[validate_file_extension])

    def __str__(self):
        return self.title


class emailservicemodel(models.Model):
    name = models.CharField(max_length = 100 )
    family = models.CharField(max_length = 100)
    email = models.EmailField(null=False , blank=False)

    def __str__(self):
        return self.email

class contact_us(models.Model):
    name = models.CharField(max_length= 64 ,default= "user")
    email = models.EmailField(null = False, blank = False)
    phone = PhoneField()
    text = models.TextField(null = False , blank = False)

    def __str__(self):
        return self.name

