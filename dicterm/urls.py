from django.conf.urls import include, url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index),
    url(r'^terme/', include('terme.urls')),
    url(r'^admin/', admin.site.urls),
]

