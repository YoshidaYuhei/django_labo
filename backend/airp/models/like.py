from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class Like(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='sender')
    citation = models.ForeignKey('Citation', on_delete=models.DO_NOTHING)
    source = models.ForeignKey('Source', on_delete=models.DO_NOTHING)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    reviewer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='reviewer')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
