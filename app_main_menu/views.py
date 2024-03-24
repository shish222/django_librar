from django.shortcuts import render


def index(req):
    req.user.is_authenticated
    return render(req, "app_main_menu/index.html", {"req": req})
