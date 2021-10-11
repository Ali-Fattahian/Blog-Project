from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from .forms import CreateUserForm

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