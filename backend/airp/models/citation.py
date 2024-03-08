from django.db import models
from accounts.models import CustomUser

class Citation(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    citation = models.TextField()
    cite_comment = models.TextField()
    category = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()
    media = models.IntegerField()
    tag_ids = models.TextField()
