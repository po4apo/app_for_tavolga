from django.contrib.auth.forms import AuthenticationForm, UsernameField

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(
            attrs={'class': "field__header", 'type': "text", 'size': "36", 'name': "name", "placeholder":"Введите ваш email"}),
        label='Логин')
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "field__header", 'type': "text", 'size': "36", 'name': "name", 'placeholder':"Введите ваш пароль"}),
        label='Пароль')
