# Generated by Django 3.0.7 on 2020-07-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20200721_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='main/')),
                ('field1', models.CharField(max_length=64)),
                ('field2', models.CharField(max_length=64)),
                ('field3', models.CharField(max_length=64)),
                ('field4', models.CharField(max_length=64)),
            ],
        ),
    ]
