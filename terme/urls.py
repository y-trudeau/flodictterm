from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from terme.views import DomaineParClient, TermeParDomaine

urlpatterns = [
    url(r'^Domaine/parClient/(?P<client>[0-9]+)/$', DomaineParClient.as_view()),
    url(r'^ParDomaine/(?P<domaine>[0-9]+)/$', TermeParDomaine.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
