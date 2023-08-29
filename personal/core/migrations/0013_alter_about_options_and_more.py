# Generated by Django 4.1.7 on 2023-08-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_about_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['name']},
        ),
        migrations.AddIndex(
            model_name='about',
            index=models.Index(fields=['-publish'], name='core_about_publish_f2b07a_idx'),
        ),
    ]
