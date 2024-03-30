from django.core.paginator import Paginator
from django.shortcuts import render

from app_add_book.models import Book


def index(req):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 1)
    page_n = req.GET.get("page")
    if not page_n:
        page_n = 1
    page_obj = paginator.get_page(page_n)
    context = {
        "req": req,
        "page": page_obj
    }

    return render(req, "app_main_menu/index.html", context)
