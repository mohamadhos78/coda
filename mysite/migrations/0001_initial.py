# Generated by Django 2.2 on 2020-05-27 13:37

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import mysite.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('cover', models.FileField(upload_to='files/category_cover/', validators=[mysite.models.validate_file_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='files/user_avatar/', validators=[mysite.models.validate_file_extension])),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='emailservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family', models.CharField(max_length=100)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('skill', models.CharField(max_length=100))
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('cover', models.FileField(upload_to='files/article_cover/', validators=[mysite.models.validate_file_extension])),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('promote', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.UserProfile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Category')),
            ],
        ),
    ]