<<<<<<< HEAD

from django.contrib import admin
from django.urls import path
from dashboard.views import index
from visitantes.views import registrar_visitante
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name='index'),
    path('registrar-visitante/', registrar_visitante ,name='registrar_visitante'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
=======
"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from dashboard.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
>>>>>>> 259bea34cf67988f3aafeb19514fc5d39454096e
]
