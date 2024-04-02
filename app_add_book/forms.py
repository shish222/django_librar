from django import forms


class UploadFileForm(forms.Form):
    name_book = forms.CharField(label="Название книги")
    name_author = forms.CharField(max_length=120, label="Имя автора")
    surname = forms.CharField(max_length=120, label="Фамилия автора")
    price = forms.IntegerField(label="Цена книги")
    genre = forms.CharField(max_length=40)
    release_date = forms.DateTimeField()
    file_text = forms.FileField(label="Файл с текстом книги")
    file_img = forms.FileField(label="Обложка книги")
