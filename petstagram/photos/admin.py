from django.contrib import admin

from petstagram.photos.models import PetPhoto


# Register your models here.
@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'created_on', 'short_description', 'all_tagged_pets')

    @staticmethod
    def all_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])

    @staticmethod
    def short_description(obj):
        return obj.description[:50]
