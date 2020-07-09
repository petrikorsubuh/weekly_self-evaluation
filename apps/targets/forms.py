from django import forms
from .models import Categories,Target

class FormCategories(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    name = forms.CharField(max_length=45,label='Name',widget=forms.TextInput(attrs={
        'class':'form-control'
    }))


class Formtarget(forms.Form):
    activity = forms.CharField(max_length=45, label='Item', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'item'
    }))
    target_set = forms.CharField(max_length=45, label='Target', widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'targets'
    }))
    unit = forms.CharField(max_length=45,label='Unit',widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'unit'
    }))
    
