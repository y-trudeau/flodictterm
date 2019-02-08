from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from terme.views import *

urlpatterns = [
		url(r'^Client/$', ClientListView.as_view()),
		url(r'^Client/(?P<pclient>[0-9-]+)/$', ClientView.as_view()),
      url(r'^ClientAjout/$', ClientAjoutView.as_view()),
      url(r'^ClientEdite/$', ClientEditionView.as_view()),
      url(r'^ClientSupprime/$', ClientSupprimeView.as_view()),
		url(r'^Domaine/parClient/(?P<client>[0-9]+)/$', DomaineParClient.as_view()),
		url(r'^parDomaine/(?P<domaine>[0-9]+)/$', TermeParDomaine.as_view()),
		url(r'^parTermeAn/(?P<termean>[0-9]+)/$', TermeParTermAn.as_view()),
		url(r'^parId/(?P<termeid>[0-9]+)/$', TermeParId.as_view()),
		url(r'^termeAnParId/(?P<termeid>[0-9]+)/$', TermeAnParId.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
