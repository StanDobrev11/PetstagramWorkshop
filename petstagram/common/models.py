from django.db import models

from petstagram.core.mixins import TimestampMixin
from petstagram.photos.models import PetPhoto


# Create your models here.
class PhotoComment(TimestampMixin):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(
        max_length=MAX_TEXT_LENGTH
    )

    to_photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.DO_NOTHING
    )
    # to_user = Foreignkey to user


class Like(models.Model):
    to_photo = models.ForeignKey(
        to=PetPhoto,
        on_delete=models.DO_NOTHING
    )

    # to_user = Foreignkey to user
