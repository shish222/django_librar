from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import AuthenForm


# Create your views here.
def authen_view(req):
    if req.method == "POST":
        form = AuthenForm(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(req, username=data["full_name"], password=data["password"])
            if user is not None:
                login(req, user)
        return redirect("/")
    else:
        form = AuthenForm()
    return render(req, "app_authen/authen.html", {"form": form})


def logout_view(req):
    logout(req)
    return redirect("/")
