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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app_add_book.views import about
from app_authen.views import authen_view, logout_view
from app_book_view.views import book_view
from app_main_menu.views import index
from app_personal_account.views import my_book_view, author_add, add_balance
from app_registration.views import registration_view

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path("ab/", about),
    path("", index),
    path("reg/", registration_view),
    path("authen/", authen_view),
    path("logout", logout_view),
    path("personal_account/", my_book_view),
    path("book/<str:name>/", book_view),
    path("<str:name>/author_add", author_add),
    path("<str:name>/add_balance/", add_balance),
    path("<str:name>/<str:name1>/add_balance/", add_balance)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
