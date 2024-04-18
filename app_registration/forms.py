from django import forms


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="ФИО")
    password = forms.CharField(label="Пароль")
    bio = forms.CharField(max_length=200, label="Ваша биография")
    img = forms.FileField(label="Аватарка")
