import uuid

from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import *


def handle_uploaded_file_text(f):
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]

    suffix = str(uuid.uuid4())
    with open(f"uploads/{name}_{suffix}{ext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f"uploads/{name}_{suffix}{ext}"


def handle_uploaded_file_img(f):
    name = f.name
    ext = ''

    if '.' in name:
        ext = name[name.rindex('.'):]
        name = name[:name.rindex('.')]

    suffix = str(uuid.uuid4())
    with open(f"media/img/{name}_{suffix}{ext}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f"img/{name}_{suffix}{ext}"


def about(request, name=True):
    if not request.user.profile.is_author:
        return render(request, "app_add_book/is_not_author.html")
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_text_path = handle_uploaded_file_text(form.cleaned_data['file_text'])
            file_img_path = handle_uploaded_file_img(form.cleaned_data['file_img'])
            book = Book(name=form.cleaned_data["name_book"], file_text=file_text_path, file_img=file_img_path,
                        price=form.cleaned_data["price"], genre=form.cleaned_data["genre"],
                        release_date=form.cleaned_data["release_date"])
            book.save()
            user = request.user.profile
            user.created_book.add(book)
            user.save()
            if name:
                return redirect('/')
            else:
                return redirect(f"{name}/")
    else:
        form = UploadFileForm()

    return render(request, 'app_add_book/about.html', {'form': form})
