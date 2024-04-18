from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
def my_book_view(req):
    profile = req.user.profile
    if req.method == "POST":
        profile.bio = req.POST["bio"]
        profile.save()
    created_book = profile.created_book.model.objects.all()
    my_book = profile.my_book.model.objects.all()
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
    return render(req, "app_personal_account/my_book.html", context=context)
