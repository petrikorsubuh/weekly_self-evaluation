from django import forms
from apps.targets.models import Target,Categories

class Edit_Achievement_Form(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput(),required=False)
    target = forms.ModelChoiceField(Target.objects.all(),label="Target",widget=forms.Select(
        attrs={
            'class':'form-control',
        }
    ))

    categories = forms.CharField(label="Category",widget=forms.TextInput(attrs={
        "class":"form-control",
    }))
    activity = forms.CharField(label="Activity",widget=forms.TextInput(attrs={
        "class":"form-control",
    }))
    target_set = forms.IntegerField(label='Target-set',widget=forms.TextInput(attrs={
        "class":"form-control",
    }))
    unit = forms.CharField(label='Unit',widget=forms.TextInput(attrs={
        "class":"form-control",
    }))
    real = forms.IntegerField(label='Actual',widget=forms.TextInput(attrs={
        "class":"form-control",
    }))
    date = forms.CharField(label="Date",widget=forms.TextInput(attrs={
        'class':'form-control',
        "id":"datepicker",
    }))
