from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from applications.views import Index

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("admin/", admin.site.urls),
    path("applications/", include("applications.urls", namespace="applications")),
    path("clients/", include("clients.urls", namespace="clients")),
    path("accounts/", include("allauth.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
