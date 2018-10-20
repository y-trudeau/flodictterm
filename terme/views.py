from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from terme.models import Client, Domaine
from terme.serializers import ClientSerializer, DomaineSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class DomaineParClient(APIView):
	def get(self, client):
		try:
			return Domaine.objects.filter(client=client)
		except Domaine.DoesNotExist:
			raise Http404
	
	def get(self, client, format=None):
		domaines = Domaine.objects.filter(client=client)
		serializer = DomaineSerializer(domaines, many=True)
		return Response(serializer.data)
