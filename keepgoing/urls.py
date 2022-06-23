from shortener.views import index, get_user#, redirect_test
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homes' ),
    #path('redirect', redirect_test),
    path('get_user/<int:user_id>', get_user)
]