from django.contrib import admin
from django.urls import path
# from .views import index
from . import views
from django.conf import settings
urlpatterns = [
    path("", views.index, name="index"),
    path("content/<int:id>/", views.content_view, name="content"),
    path("form/", views.create_article_view, name="form"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    