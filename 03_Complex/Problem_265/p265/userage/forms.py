from django import forms

class Userage(forms.Form):
    age = forms.IntegerField()