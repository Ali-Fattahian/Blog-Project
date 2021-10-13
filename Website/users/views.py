from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .models import Profile
from .forms import CreateUserForm, EditProfileForm

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.warning(request, 'You Are Already Logged In')
            return redirect('homepage')
        else:
            return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            messages.warning(request, 'Username or password is incorrect')
            return redirect('sign-in')
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'You have logged in successfully')
                return redirect('homepage')
            else:
                messages.warning(request, 'Username or password is incorrect')
                return redirect('sign-in')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
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
            messages.success(request, 'You Registered Successfully')
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
            messages.success(request, 'Saved!')
            form.save()
            return redirect('homepage')
        else:
            messages.warning(request, 'Something Went Wrong!')
            return render(request, 'users/edit-profile.html', context)