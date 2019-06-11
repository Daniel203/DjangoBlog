from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {
        'form' : form,
        'signup' : 'active',
    }
    return render(request, 'registration/signup.html', context)
