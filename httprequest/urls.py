from django.contrib import admin
from django.urls import path
from .views import data, now, SetSession, GetSession

name = 'httprequest'

urlpatterns = [
    path('', data, name='data'),
    path('now/', now, name='now'),
    path('setsession/',SetSession),
    path('getsession/',GetSession),
]
