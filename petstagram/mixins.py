from django.db import models
from django.utils import timezone


class TimestampMixin(models.Model):
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
