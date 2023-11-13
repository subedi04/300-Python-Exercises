from django import forms

class UserMarks(forms.Form):
    s1 = forms.IntegerField()
    s2 = forms.IntegerField()
    s3 = forms.IntegerField()
    s4 = forms.IntegerField()
    s5 = forms.IntegerField()
    s6 = forms.IntegerField()