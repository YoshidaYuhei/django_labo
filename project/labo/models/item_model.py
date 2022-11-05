from django.db import models
from labo.models.category_model import Category
from labo.models.user_model import User


class Item(models.Model):
    title = models.CharField(max_length=30, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=1000, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    period = models.CharField(max_length=30, null=True)
    available_hours = models.JSONField(null=True)
    available_day_of_week = models.JSONField(null=True)
    service_time = models.IntegerField(default=30)
    image_url = models.ImageField(null=True)
    sub_image_urls = models.ImageField(null=True)
    area = models.CharField(max_length=30, null=True)
    communication_style = models.JSONField(null=True)
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "items"
    
    def __str__(self) -> str:
        return self.title