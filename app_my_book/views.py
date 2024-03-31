from django.shortcuts import render


# Create your views here.
def my_book_view(req):
    return render(req, "app_personal_account/my_book.html")
