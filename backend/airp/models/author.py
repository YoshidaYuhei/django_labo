from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class Author(models.Model):
    author = models.CharField(max_length=1000)
    birth_day = models.DateTimeField(null=True, blank=True)
    categories = models.CharField(max_length=255, null=True, blank=True)
    create_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
