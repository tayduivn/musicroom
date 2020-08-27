"""musicroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from musicroom.startup import init
from musicroom.paths.index import main as index
from musicroom.paths.emailPref import main as emailPref
from musicroom.paths.login import main as login
from musicroom.paths.app import app, app_login_required
from musicroom.paths.signup import main as signup
from musicroom.paths.setName import main as setName

urlpatterns = [
    path('', index, name='index'),
    path('emailpref', emailPref, name='email_pref'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('setName', setName, name='set_name'),
    path('rooms', app_login_required, name='rooms'),
    path('createRoom', app_login_required, name='create_room'),
    path('profile/<int:user_id>', app_login_required, name='profile'),
    path('roomPreview/<int:room_id>', app_login_required, name='room_preview'),
    path('api/', include('musicroom.api.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'musicroom.paths.errors.page404'

init()
