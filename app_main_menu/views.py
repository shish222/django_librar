from django.shortcuts import render


def index(req):
    return render(req, "app_main_menu/index.html", {"req": req})
