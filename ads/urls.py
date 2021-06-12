from django.urls import path, reverse_lazy
from . import views

app_name='ads'
urlpatterns = [
    path('', views.AdListView.as_view(), name='all'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('create/',
        views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
    path('<int:pk>/update/',
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_update'),
    path('<int:pk>/delete/',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads:all')), name='ad_delete'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
