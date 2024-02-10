from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.core.mixins import TimestampMixin
from petstagram.pets.models import Pet
from petstagram.photos.validators import MaxFileSizeValidator


# Create your models here.
class PetPhoto(TimestampMixin):
    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        validators=[
            # validate_photo_size,
            MaxFileSizeValidator(limit_value=5)
        ]
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=[
            MinLengthValidator(limit_value=MIN_DESCRIPTION_LENGTH),
        ]
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )
    date_of_publication = models.DateField(
        auto_now=True,
    )

    def __str__(self):
        return self.description
