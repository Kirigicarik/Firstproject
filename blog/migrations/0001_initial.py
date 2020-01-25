# Generated by Django 2.2 on 2020-01-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='')),
                ('Content', models.CharField(max_length=1000)),
                ('Tag', models.CharField(max_length=100)),
                ('Slug', models.SlugField(max_length=20, unique=True)),
                ('Date', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
