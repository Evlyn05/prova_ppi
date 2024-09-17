"""
URL configuration for main project.

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
from core.views import index,cadastro,lista,editar_voo,remover_voo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('voo/cadastro',cadastro,name='cadastro_voo'),
    path('/lista',lista,name='lista_voo'),
    path('voo/editar/<int:id>',editar_voo,name='editar_voo'),
    path('voo/remover/<int:id>',remover_voo,name='remover_voo'),
]
