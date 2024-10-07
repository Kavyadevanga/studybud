from django.forms import ModelForm
from .models import Room
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
   
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name of your business',
                'class': 'form-control'
            }),
            'host': forms.Select(attrs={
                'class': 'chosen-select no-search-select'
            }),
            'topic': forms.Select(attrs={
                'class': 'chosen-select no-search-select'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Description of the room'
            }),
          
        }

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email-id',
        }))

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
           
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',    
                'placeholder': 'Enter Password', 
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
            }),
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("This email address is already in use.")
            return email


        def clean(self):
            cleaned_data = super().clean()
            password1 = cleaned_data.get("password1")
            password2 = cleaned_data.get("password2")

            if password1 and password2 and password1 != password2:
                raise ValidationError("Passwords do not match.")

            return cleaned_data


