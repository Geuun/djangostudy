import debug_toolbar
from django.conf.urls import include
from shortener.views import index, get_user#, redirect_test
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', index, name='homes' ),
    #path('redirect', redirect_test),
    path('get_user/<int:user_id>', get_user)
]