from django.db import models
from django.db.models.fields.files import ImageField

class Project (models.Model):
    name = models.CharField (max_length=99, null=True, blank=True)
    username = models.CharField (max_length=99, null=True, blank=True)
    email = models.CharField (max_length=99, null=True, blank=True)
    type = models.CharField (max_length=99, null=True, blank=True)
    price = models.IntegerField (null=True, blank=True)
    description = models.TextField (null=True, blank=True)
    photo=ImageField(upload_to='media/', null = True, blank = True)
    date=models.DateField(auto_now_add=True, null = True, blank = True)

    def __str__(self):
        if len(self.username) > 50:
            return self.username[:50]+"..."
        return self.username


class ProjectBuy (models.Model):
    buyer_name = models.CharField (max_length=99, null=True, blank=True)
    buyer_username = models.CharField (max_length=99, null=True, blank=True)
    buyer_email = models.CharField (max_length=99, null=True, blank=True)
    seller_name = models.CharField (max_length=99, null=True, blank=True)
    seller_username = models.CharField (max_length=99, null=True, blank=True)
    seller_email = models.CharField (max_length=99, null=True, blank=True)
    type = models.CharField (max_length=99, null=True, blank=True)
    price = models.IntegerField (null=True, blank=True)
    project = models.CharField(max_length = 99, blank = True, null = True)
    description = models.TextField (null=True, blank=True)
    photo=ImageField(upload_to='media/', null = True, blank = True)
    date=models.DateField(auto_now_add=True, null = True, blank = True)

    def __str__(self):
        if len(self.buyer_name) > 50:
            return self.buyer_name[:50]+"..."
        return self.buyer_name

class JobApplication(models.Model):
    CATEGORIES = (
        ('Graphics Designer', 'Graphics Designer'),
        ('Web Developer', 'Web Developer'),
        ('Content Writing', 'Content Writing'),
    )

    category = models.CharField(max_length=50, choices=CATEGORIES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    cv = models.FileField(upload_to='cv/')
    photo = models.ImageField(upload_to='photos/')
    education = models.CharField(max_length=100)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

