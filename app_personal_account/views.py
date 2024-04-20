from django.shortcuts import render, Http404, redirect
from django.core.paginator import Paginator
from .forms import *


# Create your views here.
def my_book_view(req):
    profile = req.user.profile
    if req.method == "POST":
        profile.bio = req.POST["bio"]
        profile.save()
    created_book = profile.created_book.all()
    my_book = profile.my_book.all()
    page_n = req.GET.get("page")
    paginator_created_book = Paginator(created_book, 4)
    paginator_my_book = Paginator(my_book, 4)
    page_my_b = paginator_my_book.get_page(page_n)
    page_cr = paginator_created_book.get_page(page_n)
    bio_l = []
    c = 0
    if len(profile.bio) < 30:
        bio_l.append(profile.bio)
    for i in range(0, len(profile.bio), 30):
        bio_l.append(profile.bio[c:i])
        c = i
    bio = "\n".join(bio_l)
    context = {
        "profile": profile,
        "page_created": page_cr,
        "page_my_b": page_my_b,
        "bio_l": bio_l,
        "bio": bio,
    }
    return render(req, "app_personal_account/personal_account.html", context=context)


def author_add(req, name):
    if not req.user.profile.is_author:
        profile = req.user.profile
        if profile.balance >= 500:
            profile.balance -= 500
            profile.is_author = True
            profile.save()
            return redirect(f"/{name}")
        else:
            return render(req, "app_personal_account/not_balance.html")
    else:
        return Http404


def add_balance(req, name, name1=""):
    if req.method == "POST":
        form = BalanceForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            profile = req.user.profile
            profile.balance += data["incr"]
            profile.save()
        return redirect(f"/{name}/{name1}")
    else:
        form = BalanceForm()
    context = {
        "form": form
    }
    return render(req, "app_personal_account/add_balance.html", context=context)
