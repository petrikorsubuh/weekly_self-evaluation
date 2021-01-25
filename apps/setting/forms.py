from django import forms

class Querydate(forms.Form):
    set_property = forms.CharField()
    value = forms.CharField()

class SearchDateForm(forms.Form):
    start_date = forms.CharField(label="Start Date", widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'id':'datepicker'
    }))
    end_date = forms.CharField(label="End Date", widget=forms.TextInput(attrs={
        'class':'form-control',
        'type':'text',
        'id':'datepicker2'
    }))

