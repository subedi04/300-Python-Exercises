from dataclasses import field
from django import forms
from . models import StdInfo

class StdForm(forms.ModelForm):
    class Meta:
        model = StdInfo
        fields = "__all__"
