from django.db import models
from django.contrib.auth.models import AbstractUser
from labo.models.category_model import Category


class User(AbstractUser):
    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
        OTHER = 3
    
    sing_in_count = models.IntegerField(default=0)
    facebook_url = models.URLField(null=True)
    facebook_token = models.CharField(max_length=200, null=True)
    birth_day = models.DateField(null=True)
    description = models.TextField(null=True)
    nickname = models.CharField(max_length=100, null=True)
    gender = models.IntegerField(choices=Gender.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    backgroun_image = models.ImageField(null=True)
    avatar = models.ImageField(null=True)
    excel = models.FileField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    categories = models.ManyToManyField(Category)
    remarks = models.JSONField(null=True)
    deleted = models.BooleanField(null=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self) -> str:
        return self.username
