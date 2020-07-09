from django import forms
from .models import Profile

class RegisterForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    GENDER =(
        ('D',''),
        ('L','MALE'),
        ('P','FEMALE')
    )
    username = forms.CharField(label='Username',max_length=15,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'username'
    }))
    password1 = forms.CharField(label='Password',max_length=45,widget=forms.TextInput(attrs={
        'placeholder':'password',
        'class':'form-control',
        'type':'password'
    }))
    password2 = forms.CharField(label='Confirmation Password',max_length=45,widget=forms.TextInput(attrs={
        'placeholder':'confirmation password',
        'class':'form-control',
        'type':'password'
    }))
    firstname = forms.CharField(label='First Name',max_length=15,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'first name'
    }))
    lastname = forms.CharField(label='Last Name',max_length=15,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'last name'
    }))
    age = forms.CharField(label='age',max_length=5,widget=forms.TextInput(attrs={
        'placeholder':'age',
        'class':'form-control'
    }))
    gender = forms.ChoiceField(label='gender',choices=GENDER,widget=forms.Select(attrs={
        'class':'form-control',
    }))
    photo_profile = forms.ImageField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=13,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password = forms.CharField(label='Password',max_length=13,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'********',
        'type':'password'

    }))