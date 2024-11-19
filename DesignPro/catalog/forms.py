from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="",
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Имя пользователя'
        })
    )
    password = forms.CharField(label="", widget=forms.PasswordInput)