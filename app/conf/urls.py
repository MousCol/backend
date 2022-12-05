"""mous URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from views.login import Login
from views.signup import Signup
from views.barberies import Barberies
from views.services import Services
from views.schedule import Schedule

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
    path('barberies/', Barberies.as_view()),
    path('services/', Services.as_view()),
    path('schedule/', Schedule.as_view()),
]
