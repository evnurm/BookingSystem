from django import forms
from .models import Item


class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Title'})}
        exclude = []