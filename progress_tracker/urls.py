from django.contrib import admin
from django.urls import path, include

from progress_tracker.admin import configure_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crackmes/', include('crackmes.urls')),
    path('auth/', include('auth.urls')),
    path('user/', include('user.urls'))
]

configure_admin_site()