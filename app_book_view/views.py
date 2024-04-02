from django.shortcuts import render

from app_add_book.models import Book


# Create your views here.
def book_view(req, name):
    book_obj = Book.objects.get(name=name)
    file_name = book_obj.file_text
    with open(file_name.name, "r") as f:
        text = f.read()
    context = {
        "name": name,
        "text": text.split("\n")
    }
    return render(req, "app_book_view/book.html", context)
