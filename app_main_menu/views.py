from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import FilterForm
from app_add_book.models import Book


def index(req):
    if req.method == "POST":
        form = FilterForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            book_list = Book.objects.filter(genre=data["genre"], name__icontains=data["name"])
    else:
        form = FilterForm()
        book_list = Book.objects.all()
    paginator = Paginator(book_list, 8)
    page_n = req.GET.get("page")
    if not page_n:
        page_n = 1
    page_obj = paginator.get_page(page_n)
    context = {
        "req": req,
        "page": page_obj,
        "form": form
    }

    return render(req, "app_main_menu/index.html", context)
