"""
URL configuration for agendamento_pagamento project.

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
from agendamentos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/agendamentos/', views.criar_agendamento, name='criar_agendamento'),
    path('api/listar-agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('api/agendamentos/<int:id>/', views.consultar_agendamento, name='consultar_agendamento'),
    path('api/deletar-agendamento/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),
]
