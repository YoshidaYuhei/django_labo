from django.utils import timezone
from django.db import models
from accounts.models import CustomUser


class CiteReview(models.Model):
    reviewer_id = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    citation_id = models.ForeignKey('Citation', on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateField(default=timezone.now())
    updated_at = models.DateField(default=timezone.now())
