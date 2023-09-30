from django import forms


class Myform(forms.Form):
    name = forms.CharField(max_length=100)
    Email = forms.EmailField()
    age = forms.IntegerField()
    