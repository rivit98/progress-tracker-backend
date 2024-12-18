from django.contrib import admin
from django.urls import include, path

from progress_tracker.admin import configure_admin_site

urlpatterns = [
    path("admin/", admin.site.urls),
    path("crackmes/", include("crackmes.urls")),
    path("heroes_maps/", include("heroes3maps.urls")),
    path("games/", include("games.urls")),
    path("auth/", include("auth.urls")),
    path("user/", include("user.urls")),
]

configure_admin_site()
