from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(max_length=MAX_NAME_LENGTH)
    photo_address = models.URLField()
    birth_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(null=False, blank=True, unique=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)

