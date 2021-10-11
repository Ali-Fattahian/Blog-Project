from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        labels = {
            'username':'Username',
            'password1':'Password',
            'password2':'Password Confirmation'
        }