# Generated by Django 4.1.7 on 2023-08-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_post_links_project_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
