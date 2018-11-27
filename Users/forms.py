from django import forms
from django.contrib.auth.models import User


# Form for logging in.
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class SignupForm(forms.ModelForm):
    password_again = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Re-type password'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'})
        }

    field_order = ['username', 'password', 'password_again', 'email']

    def clean_password_again(self):
        if self.cleaned_data['password'] != self.cleaned_data['password_again']:
            raise forms.ValidationError("Passwords do not match!")
        else:
            return self.cleaned_data['password_again']
