from django.contrib import admin
from django.urls import path, include
import core.urls as apis

urlpatterns = [
    path('api/', include(apis)),
    path('admin/', admin.site.urls),
]
