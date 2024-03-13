from django.utils import timezone
from django.db import models
from accounts.models import CustomUser
from airp.models.abstract import BaseModel

class Source(BaseModel):
    source = models.CharField(max_length=1000)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    category = models.IntegerField(null=True, blank=True)
    create_user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
