from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from terme.models import Client, Domaine, TermeAn, TermeFr
from terme.serializers import ClientSerializer, DomaineSerializer, TermeAnSerializer, TermeFrSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class DomaineParClient(APIView):
	def get(self, request, client):
		try:
			return Domaine.objects.filter(client=client)
		except Domaine.DoesNotExist:
			raise Http404
	
	def get(self, request, client, format=None):
		domaines = Domaine.objects.filter(client=client)
		serializer = DomaineSerializer(domaines, many=True)
		return Response(serializer.data)

class TermeParDomaine(APIView):
	def get(self, request, domaine):
		try:
			return TermeAn.objects.filter(domaine=domaine)
		except TermeAn.DoesNotExist:
			raise Http404
	
	def get(self, request, domaine, format=None):
		termes = TermeAn.objects.filter(domaine=domaine)
		serializer = TermeAnSerializer(termes, many=True)
		return Response(serializer.data)

class TermeParTermAn(APIView):
	def get(self, request, termean):
		try:
			return TermeFr.objects.filter(termeAn=termean)
		except TermeFr.DoesNotExist:
			raise Http404
	
	def get(self, request, termean, format=None):
		termes = TermeFr.objects.filter(termeAn=termean)
		serializer = TermeFrSerializer(termes, many=True)
		return Response(serializer.data)
