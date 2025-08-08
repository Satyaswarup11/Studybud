from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']  # Specify the fields you want to include in the form


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'  # This will include all fields from the Room model
        exclude = ['host', 'participants']  # Exclude fields that should not be set by the form
    
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username', 'email' ]  # Specify the fields you want to include in the form