# Generated by Django 5.0 on 2024-01-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_phto_project_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]