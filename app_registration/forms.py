from django import forms


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="ФИО")
    password = forms.CharField(label="Пароль")
    img = forms.FileField(label="Аватарка")
