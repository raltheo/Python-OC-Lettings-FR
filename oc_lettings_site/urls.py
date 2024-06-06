from django.contrib import admin
from django.urls import path

from . import views
from profiles import views as profilesviews
from lettings import views as lettingsviews

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", lettingsviews.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", lettingsviews.letting, name="letting"),
    path("profiles/", profilesviews.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", profilesviews.profile, name="profile"),
    path("admin/", admin.site.urls),
]

handler404 = "oc_lettings_site.views.custom_404"
handler500 = "oc_lettings_site.views.custom_500"
