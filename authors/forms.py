from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        #exclude =
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password'
        }
        help_texts = {
            'first_name': 'Enter your first name.',
            'last_name': 'Enter your last name.',
            'username': 'Enter a username.',
            'email': 'Enter your email address.',
            'password': 'Enter a password.'
        }
        error_messages = {
            username: {
                'unique': "This username is already taken. Please choose a different one.",
            },
            
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'type your first name here',
                                                'class': 'input text-input outra-classe'                                                
                                                 }),
            'password': forms.PasswordInput(attrs={'placeholder': 'type your password here',})
        
        }