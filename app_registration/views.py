import uuid

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app_add_book.models import Profile
from .forms import RegistrationForm


def handle_uploaded_file_img(f):
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]

    suffix = str(uuid.uuid4())
    with open(f"media/img_pr/{name}_{suffix}{ext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f"img_pr/{name}_{suffix}{ext}"


# Create your views here.
def registration_view(req):
    if req.method == "POST":
        form = RegistrationForm(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data
            img_path = handle_uploaded_file_img(data["img"])
            user = User.objects.create_user(password=data["password"], username=data["full_name"])
            user.save()
            profile = Profile(user=user, name=data["full_name"], img=img_path, bio=data["bio"])
            profile.save()

            login(req, user)
            return redirect("/")
    else:
        form = RegistrationForm
    return render(req, "app_registration/reg.html", {"form": form})
