from django.shortcuts import render, redirect


# Create your views here.
def signup_user(request):
    context = {}
    return render(request, 'accounts/signup_page.html', context)


def signin_user(request):
    context = {}
    return render(request, 'accounts/signin_page.html', context)


def signout_user(request):
    """ does not need view """
    # logic for sign out
    return redirect('index')


def details_profile(request, pk):
    context = {}
    return render(request, 'accounts/details_profile.html', context)


def edit_profile(request, pk):
    context = {}
    return render(request, 'accounts/edit_profile.html', context)


def delete_profile(request, pk):
    context = {}
    return render(request, 'accounts/delete_profile.html', context)
