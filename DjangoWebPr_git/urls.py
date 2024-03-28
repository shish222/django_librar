"""
DjangoWebPr_git URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path

from app_add_book.views import about
from app_authen.views import authen_view, logout_view
from app_main_menu.views import index
from app_personal_account.views import pers_acc_view
from app_registration.views import registration_view

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path("ab/", about),
    path("", index),
    path("reg/", registration_view),
    path("authen/", authen_view),
    path("logout", logout_view),
    path("personal_account/", pers_acc_view),
]
