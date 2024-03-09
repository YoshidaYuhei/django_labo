from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class Citation(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    citation = models.TextField()
    cite_comment = models.TextField(null=True, blank=True)
    category = models.IntegerField(null=True, blank=True)
    media = models.IntegerField()
    tag_ids = models.TextField(null=True, blank=True)
    created_at = models.DateField(default=timezone.now())
    updated_at = models.DateField(default=timezone.now())
