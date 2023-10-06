"""
URL configuration for ultima project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# Importando todas as views definidas no arquivo 'views.py' da app 'base'
# O * importa todos os métodos de views
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('contato/', contato, name="contato"),
    path('reserva/', reserva, name="reserva"),
    # url adicionada para ser renderizada na index.html do projeto
    path('login/', login_usuario, name="login_usuario"),
    path('logout/', logout_usuario, name="logout_usuario"),
]
