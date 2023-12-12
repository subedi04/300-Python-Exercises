from django import forms

class StudentList(forms.Form):
    std1 = forms.CharField(max_length=100)
    std2 = forms.CharField(max_length=100)
    std3 = forms.CharField(max_length=100)
    std4 = forms.CharField(max_length=100)
    std5 = forms.CharField(max_length=100)
