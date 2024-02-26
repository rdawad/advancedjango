from django import forms


class FormClass(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)