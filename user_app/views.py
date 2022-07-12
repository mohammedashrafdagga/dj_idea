from django.http import HttpResponse
from django.shortcuts import redirect, render

from user_app.models import Profile
from .forms import ProfileForm, UserForm
from django.contrib.auth import authenticate, login
# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            profile = Profile.objects.get(user=request.user)
            pforms = ProfileForm(request.POST, request.FILES, instance=profile)
            if pforms.is_valid():
                pforms.save()
            return redirect('user_app:main_fun')
        else:
            print('Error')
    return render(request, 'registration/sign_up.html')


def main(request):

    return HttpResponse(str(f'Hello User  {request.user.first_name} {request.user.last_name} in app.'))
