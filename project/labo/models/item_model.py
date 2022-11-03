from django.db import models
from labo.models.category_model import Category
from labo.models.user_model import CustomUser

class Item(models.Model):
    title = models.CharField(max_length=30, null=True)
    content = models.TextField(max_length=1000, null=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = "items"