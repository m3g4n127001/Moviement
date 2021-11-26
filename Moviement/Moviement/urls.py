from django import urls
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = "home"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('',include('movies.urls'),name="homepage"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)