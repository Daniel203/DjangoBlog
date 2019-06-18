from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import UserCreateForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = UserCreateForm()

    context = {
        'form' : form, 
        'signup' : 'active', 
    }
    return render(request, 'registration/signup.html', context)


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile/user_settings.html')
   
    else:
        return render(request, 'user_profile/user_not_logged.html')

