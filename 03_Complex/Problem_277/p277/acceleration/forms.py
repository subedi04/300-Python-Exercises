from django import forms

class FindAcce(forms.Form):
    v = forms.FloatField()
    t = forms.FloatField()