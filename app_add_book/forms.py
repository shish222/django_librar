from django import forms


class UploadFileForm(forms.Form):
    name_book = forms.CharField(label="Название книги")
    price = forms.IntegerField(label="Цена книги")
    genre = forms.CharField(max_length=40)
    release_date = forms.DateField()
    file_text = forms.FileField(label="Файл с текстом книги")
    file_img = forms.FileField(label="Обложка книги")
