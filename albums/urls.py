from django.urls import path, reverse_lazy
from . import views

app_name = 'albums'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('upload', views.upload_image_view, name='upload_image_view'),

]
