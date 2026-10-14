from dataclasses import field

from django import forms
from django.contrib.auth.models import User

def add_attr(self, attr_name, attr_new_val):
        existing_attr = field.widget.attrs.get(attr_name, '')
        field.widget.attrs[attr_name] = f"{existing_attr} {attr_new_val}".strip()
        
        
def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)

class RegisterForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs): 
        super.__init__(*args, **kwargs)
        add_placeholder(self.fields['username'],' your username here')
        add_placeholder(self.fields['email'], ' your email')
        add_placeholder(self.fields['first_name'], ' your first name here')
        add_placeholder(self.fields['last_name'], ' your last name here')
        add_placeholder(self.fields['password'], ' your password here')
        add_placeholder(self.fields['password2'], ' repeat your password here')
        
    
           
    password = forms.CharField(required=True, 
                                    widget=forms.PasswordInput(attrs={'placeholder': 'your password here'}),
                                    error_messages={'required': 'Please enter a password.'},
                                    help_text='required': '8 characters or more. Letters, digits and @/./+/-/_ only.'
                                    )
    
    password2 = forms.CharField(required=True, 
                                widget=forms.PasswordInput(attrs={'placeholder': 'repeat your password here'})
                                )
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