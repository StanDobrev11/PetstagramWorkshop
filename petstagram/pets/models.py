from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(max_length=MAX_NAME_LENGTH)
    photo_address = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(null=False, blank=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        # must call super().save() first in order to save the instance and then be able to use its ID.
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
