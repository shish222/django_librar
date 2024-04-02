from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app_add_book.models import Profile
from .forms import RegistrationForm


# Create your views here.
def registration_view(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(password=data["password"], username=data["full_name"])
            name = data["full_name"].split()[1]
            surname = data["full_name"].split()[0]
            profile = Profile(user=user, name=name, surname=surname)
            profile.save()
            user.save()
            login(req, user)
            return redirect("/")
    else:
        form = RegistrationForm
    return render(req, "app_registration/reg.html", {"form": form})
