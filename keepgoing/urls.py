from shortener.views import index, redirect_test, get_user
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='homes' ),
    #path('redirect', redirect_test),
    pathr('get_user/<int:user_id>', get_user)
]