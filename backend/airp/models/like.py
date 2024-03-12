from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class Like(models.Model):
    sender_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='sender')
    citation_id = models.ForeignKey('Citation', on_delete=models.DO_NOTHING)
    source_id = models.ForeignKey('Source', on_delete=models.DO_NOTHING)
    author_id = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    reviewer_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name='reviewer')
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)
