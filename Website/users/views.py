from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from .models import Profile
from .forms import CreateUserForm, EditProfileForm

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            print('can\'t find the username')
            return redirect('sign-in')
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                print('can\'t find the password')
                return redirect('sign-in')

def logout_view(request):
    logout(request)
    return redirect('homepage')

class SignUpView(View):
    def get(self, request):
        form = CreateUserForm()
        context = {'form':form}
        return render(request, 'users/sign-up.html', context)

    def post(Self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'users/sign-up.html', {'form':form})


class EditProfileView(View):
    def get(self, request, slug):
        profile = get_object_or_404(Profile, slug=slug)
        form = EditProfileForm(instance=profile)
        context = {'form':form, 'profile':profile}
        return render(request, 'users/edit-profile.html', context)

    def post(self, request, slug):
        profile = get_object_or_404(Profile, slug=slug)
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        context = {'form':form, 'profile':profile}
        if form.is_valid():
            print('yay')
            form.save()
            return redirect('homepage')
        else:
            return render(request, 'users/edit-profile.html', context)