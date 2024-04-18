from django import forms
from app_add_book.models import Book


class FilterForm(forms.Form):
    name = forms.CharField(label="Название")
    book_list = Book.objects.all()
    genre = []
    for i in range(len(book_list)):
        genre.append((book_list[i].genre, book_list[i].genre))
    print(genre)
    genre = forms.ChoiceField(choices=tuple(genre), label="Жанр")
