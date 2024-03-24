from django import forms


class UploadFileForm(forms.Form):
    name_book = forms.CharField(label="Название книги")
    name_author = forms.CharField(max_length=30, label="Имя автора")
    surname = forms.CharField(max_length=30, label="Фамилия автора")
    price = forms.IntegerField(label="Цена книги")
    file = forms.FileField(label="Файл с текстом книги")
