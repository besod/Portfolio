# Generated by Django 4.1.7 on 2023-08-29 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_about_body_about_created_about_image_about_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='slug',
        ),
    ]
