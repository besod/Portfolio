# Generated by Django 4.1.7 on 2023-08-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_project_publish'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='project',
            name='core_projec_created_25e517_idx',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['-publish'], name='core_projec_publish_9fd543_idx'),
        ),
    ]
