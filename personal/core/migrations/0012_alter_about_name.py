# Generated by Django 4.1.7 on 2023-08-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_about_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
