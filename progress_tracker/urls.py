from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crackmes/', include('crackmes.urls')),
    path('auth/', include('auth.urls')),
    path('user/', include('user.urls'))
]
