from django import forms

class UserForce(forms.Form):
    m = forms.FloatField()
    a = forms.FloatField()