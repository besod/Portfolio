# Generated by Django 4.1.7 on 2023-09-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_post_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.TextField(default=True),
        ),
    ]