from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView

app_name = 'imgs'

urlpatterns = [
    path('', views.ImgListView.as_view(), name='all'),
    path('img/<int:pk>', views.ImgDetailView.as_view(), name='img_detail'),
    path('img/create',
         views.ImgCreateView.as_view(success_url=reverse_lazy('imgs:all')), name='img_create'),
    path('img/<int:pk>/update',
         views.ImgUpdateView.as_view(success_url=reverse_lazy('imgs:all')), name='img_update'),
    path('img/<int:pk>/delete',
         views.ImgDeleteView.as_view(success_url=reverse_lazy('imgs:all')), name='img_delete'),
    path('img/<int:pk>/stream', views.stream_file, name='img_stream'),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
