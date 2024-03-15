# Generated by Django 5.0 on 2024-01-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_projectbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Graphics Designer', 'Graphics Designer'), ('Web Developer', 'Web Developer'), ('Content Writing', 'Content Writing')], max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=100)),
                ('cv', models.FileField(upload_to='cv/')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('education', models.CharField(max_length=100)),
                ('experience', models.TextField(blank=True, null=True)),
            ],
        ),
    ]