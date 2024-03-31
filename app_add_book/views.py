import uuid

from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import *


def handle_uploaded_file(f):
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


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(form.cleaned_data['file'])
            print(form.cleaned_data)
            aut = Admin(name=form.cleaned_data["name_author"], surname=form.cleaned_data["surname"])
            aut.save()
            # aut = Admin.objects.create(name=form.cleaned_data["name_author"], surname=form.cleaned_data["surname"])
            bk = Book(name=form.cleaned_data["name_book"], file=file_path, price=form.cleaned_data["price"])
            bk.save()
            bk.auth.add(aut)
            return redirect('/')
    else:
        form = UploadFileForm()

    return render(request, 'app_add_book/about.html', {'form': form})
