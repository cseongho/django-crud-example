from django import forms


class createForm(forms.Form):
    photo = forms.ImageField(label="crud")
