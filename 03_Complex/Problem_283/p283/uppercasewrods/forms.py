from django import forms

class WordsList(forms.Form):
    w1 = forms.CharField(max_length=100)
    w2 = forms.CharField(max_length=100)
    w3 = forms.CharField(max_length=100)
    w4 = forms.CharField(max_length=100)
    w5 = forms.CharField(max_length=100)
