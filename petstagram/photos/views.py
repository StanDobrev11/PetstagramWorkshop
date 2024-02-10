from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from petstagram.common.models import Like
from petstagram.photos.models import PetPhoto


# Create your views here.
def add_photo(request):
    context = {}
    return render(request, 'photos/add_photo.html', context)


def edit_photo(request, pk):
    context = {}
    return render(request, 'photos/edit_photo.html', context)


def photo_details(request, pk):
    context = {
        'photo': PetPhoto.objects.get(pk=pk),
    }
    return render(request, 'photos/photo_details.html', context)


def delete_photo(request, pk):
    context = {}
    return render(request, 'photos/delete_photo.html', context)


def like_photo(request, pk):
    # pet_photo = PetPhoto.objects.get(pk=pk, user=request.user)
    if not request.user.is_authenticated:
        return redirect('signin user')

    pet_photo = get_object_or_404(PetPhoto, pk=pk)
    photo_like = Like.objects.filter(to_photo=pet_photo).first()

    if photo_like:  # already liked and we must dislike it
        photo_like.delete()

    else:
        Like.objects.create(to_photo=pet_photo)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/default/path/if/referer/not/set'))

