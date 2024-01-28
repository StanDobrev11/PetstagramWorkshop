import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petstagram.settings")
django.setup()

# Import your models
from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto

print()

