from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("authentication.urls")),
    path("home/", include("qr_gen_app.urls")),
]
