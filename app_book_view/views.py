from django.shortcuts import render, redirect

from app_add_book.models import Book


# Create your views here.
def book_view(req, name):
    profile = req.user.profile
    book_obj = Book.objects.get(name=name)
    if req.method == "POST":
        if profile.balance >= book_obj.price:
            author = book_obj.created_book.all()[0]
            author.balance += book_obj.price
            author.save()
            profile.balance -= book_obj.price
            profile.my_book.add(book_obj)
            profile.save()
            return redirect(f"/book/{name}")
        else:
            return render(req, "app_personal_account/not_balance.html")
    if req.user.is_authenticated:
        if book_obj in profile.my_book.all() or book_obj in profile.created_book.all():
            file_name = book_obj.file_text
            with open(file_name.name, "r") as f:
                text = f.read()
            context = {
                "name": name,
                "text": text.split("\n")
            }
            return render(req, "app_book_view/book.html", context)
        else:
            return render(req, "app_book_view/buy_book.html", context={"price": book_obj.price})

    else:
        return render(req, "app_book_view/redirect_auth.html")
