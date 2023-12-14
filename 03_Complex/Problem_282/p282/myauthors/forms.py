from django import forms

class AuthorBooks(forms.Form):
    auth1 = forms.CharField(max_length=100)
    book1 = forms.CharField(max_length=100)
    auth2 = forms.CharField(max_length=100)
    book2 = forms.CharField(max_length=100)
    auth3 = forms.CharField(max_length=100)
    book3 = forms.CharField(max_length=100)
