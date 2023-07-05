from django.contrib import admin
from django.urls import path
# from .views import index
from . import views
from django.conf import settings
urlpatterns = [
    path("", views.index, name="index"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    