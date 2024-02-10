from django.shortcuts import render, redirect

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.
def add_pet(request):
    pet_form = PetCreateForm(request.POST or None)

    if request.method == 'POST':
        if pet_form.is_valid():
            added_pet = pet_form.save()
            return redirect('details pet', username=request.user, pet_slug=added_pet.slug)

    context = {
        'pet_form': pet_form,
    }
    return render(request, 'pets/add_pet.html', context)


def delete_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    pet_form = PetDeleteForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        pet_form.save()
        return redirect('index')

    context = {
        'pet': pet,
        'pet_form': pet_form,
    }
    return render(request, 'pets/delete_pet.html', context)


def details_pet(request, username, pet_slug):
    context = {
        'pet': Pet.objects.get(slug=pet_slug),
    }
    return render(request, 'pets/pet_details.html', context)


def edit_pet(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)

    pet_form = PetEditForm(request.POST or None, instance=pet)

    if request.method == 'POST':
        if pet_form.is_valid():
            pet_form.save()
            return redirect('edit pet', username=username, pet_slug=pet_slug)

    context = {
        'pet': pet,
        'username': username,
        'pet_form': pet_form,
    }
    return render(request, 'pets/edit_pet.html', context)
