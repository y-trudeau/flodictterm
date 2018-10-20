from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from terme.views import DomaineParClient

urlpatterns = [
    url(r'^Domaine/(?P<client>[0-9]+)/$', DomaineParClient.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
