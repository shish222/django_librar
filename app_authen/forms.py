from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms


class AuthenForm(forms.Form):
    full_name = forms.CharField(max_length=120, label='ФИО')
    password = forms.CharField(label='Пароль')

