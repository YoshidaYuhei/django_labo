from django.db import models

class BaseModel(models.Model):
    class Meta:
        abstract = True

    def to_dict(self):
        return {f: getattr(self, f) for f in self.__dict__.keys() if f != '_state'}
