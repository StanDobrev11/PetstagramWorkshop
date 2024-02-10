from django.shortcuts import render

from petstagram.photos.models import PetPhoto


# Create your views here.
def index(request):
    context = {
        'pet_photos': PetPhoto.objects.all()
    }
    return render(request, 'common/index.html', context)
