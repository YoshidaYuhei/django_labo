from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def to_dict(self):
        fields = [f.name for f in self._meta.get_fields()]
        return {f: getattr(self, f) for f in fields if f != '_state'}
