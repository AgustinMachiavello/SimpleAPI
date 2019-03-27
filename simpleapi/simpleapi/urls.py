from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0.1/', include('simpleapi.apps.api.urls'))
]
