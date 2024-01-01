"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ProjectA.learning_logs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('try/', views.Try),
    path('design/', views.Design, name='design'),
    path('description/', views.Description, name='description'),
    path("Ark_login/", views.Ark_Login, name="Ark_Login"),
    path('frame/', views.Frame, name='Frame')
]
