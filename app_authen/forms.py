from django import forms


class AuthenForm(forms.Form):
    full_name = forms.CharField(max_length=120, label="ФИО")
    password = forms.CharField(label="Пароль")
