from shortener.views import index, redirect_test
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home' ),
    path('redirect', redirect_test),
]