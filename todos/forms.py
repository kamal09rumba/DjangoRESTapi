from django import forms
from .models import Todo
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title','completed')

# user registration form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:   #it is information about class
        model = User
        fields = ['username','password','email']
