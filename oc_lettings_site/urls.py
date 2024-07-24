from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("trigger-error", views.trigger_500),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path("admin/", admin.site.urls),
]

handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"
