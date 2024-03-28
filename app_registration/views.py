from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegistrationForm


# Create your views here.
def registration_view(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(password=data["password"], username=data["full_name"])
            user.save()
            login(req, user)
            return redirect("/")
    else:
        form = RegistrationForm
    return render(req, "app_registration/reg.html", {"form": form})
