from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class Source(models.Model):
    source = models.CharField(max_length=1000)
    author_id = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    category = models.IntegerField(null=True, blank=True)
    create_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateField(default=timezone.now())
    updated_at = models.DateField(default=timezone.now())
