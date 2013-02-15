from django import forms

from braces.forms import UserKwargModelFormMixin


class ExampleForm(UserKwargModelFormMixin, forms.Form):
    text = forms.CharField()
