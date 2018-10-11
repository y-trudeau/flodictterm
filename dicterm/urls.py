from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^terme/', include('terme.urls')),
    url(r'^admin/', admin.site.urls),
]

