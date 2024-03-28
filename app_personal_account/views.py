from django.shortcuts import render


# Create your views here.
def pers_acc_view(req):
    return render(req, "app_personal_account/pers_acc.html")
