# Generated by Django 4.1.7 on 2023-08-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_about_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='links',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]