from django import forms

class AppForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.CharField(max_length=80)
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
