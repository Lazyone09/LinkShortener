from django import forms

class IsGay(forms.Form):
    isgay = forms.BooleanField()