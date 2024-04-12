from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
def my_book_view(req):
    profile = req.user.profile
    created_book = profile.created_book.model.objects.all()
    page_n = req.GET.get("page")
    paginator = Paginator(created_book, 4)
    page_cr = paginator.get_page(page_n)
    context = {
        "profile": profile,
        "page_created": page_cr,
    }
    return render(req, "app_personal_account/my_book.html", context=context)
