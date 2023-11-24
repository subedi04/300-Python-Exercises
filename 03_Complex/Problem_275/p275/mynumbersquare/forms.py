from django import forms

class UserNumber(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()