from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=1000)
    
    class Meta:
        db_table = "items"