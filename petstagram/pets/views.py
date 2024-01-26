from django.shortcuts import render


# Create your views here.
def add_pet(request):
    context = {}
    return render(request, 'pets/add_pet.html', context)


def delete_pet(request, username, pet_slug):
    context = {}
    return render(request, 'pets/delete_pet.html', context)


def details_pet(request, username, pet_slug):
    context = {}
    return render(request, 'pets/pet_details.html', context)


def edit_pet(request, username, pet_slug):
    context = {}
    return render(request, 'pets/edit_pet.html', context)
