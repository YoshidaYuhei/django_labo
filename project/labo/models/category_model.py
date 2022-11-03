from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, null=True)
    content = models.TextField(max_length=1000, null=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = "categories"