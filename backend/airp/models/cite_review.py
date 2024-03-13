from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class CiteReview(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    citation = models.ForeignKey('Citation', on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
