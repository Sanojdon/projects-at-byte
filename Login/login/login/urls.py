from django.contrib import admin
from django.urls import path,include
from two_factor.urls import urlpatterns as tf_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls') )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
