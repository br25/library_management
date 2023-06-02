from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include('library_auth.urls')),
    path("api/", include('library_app.urls')),
]
