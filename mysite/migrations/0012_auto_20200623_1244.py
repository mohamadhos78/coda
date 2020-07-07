# Generated by Django 3.0.7 on 2020-06-23 12:44

from django.db import migrations, models
import mysite.models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20200603_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.FileField(upload_to='article_cover/', validators=[mysite.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=models.FileField(upload_to='category_cover/', validators=[mysite.models.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to='user_avatar/', validators=[mysite.models.validate_file_extension]),
        ),
    ]