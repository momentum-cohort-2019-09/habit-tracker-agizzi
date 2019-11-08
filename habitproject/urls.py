
from django.contrib import admin
from django.urls import path, include
from goalkeeper import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('goalkeeper.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.index, name="base"),
]
