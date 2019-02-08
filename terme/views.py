from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from terme.models import *
from terme.serializers import *
from django.http import Http404, HttpResponse
from rest_framework import status

# Create your views here.

class ClientAjoutView(APIView):
	def post(self, request, format=None):
		nomClient = request.data['nom_client']
		nouvClient = Client(nom_client = nomClient)
		nouvClient.save()
		serializer = ClientSerializer(nouvClient, many=False)
		return Response(serializer.data)

class ClientEditionView(APIView):
	def post(self, request, format=None):
		try:
			updClientId = request.data['id']
			updClient = Client.objects.get(pk=updClientId)
			updClient.nom_client = request.data['nom_client']
			updClient.save()
			serializer = ClientSerializer(updClient, many=False)
			return Response(serializer.data)
		except Client.DoesNotExist:
			raise Http404

class ClientSupprimeView(APIView):
	def post(self, request, format=None):
		try:
			delClientId = request.data['id']
			delClient = Client.objects.get(pk=delClientId)
			delClient.delete()
			serializer = ClientSerializer(delClient, many=False)
			return Response(serializer.data)
		except Client.DoesNotExist:
			raise Http404
   
class ClientView(APIView):
	def get(self, request, pclient, format=None):
		try:
			if pclient == "0":
				listClient = Client.objects.all()
				serializer = ClientSerializer(listClient, many=True)
			else:
				listClient = Client.objects.get(pk=pclient)
				serializer = ClientSerializer(listClient, many=False)
			return Response(serializer.data)
		except Client.DoesNotExist:
			raise Http404

class ClientListView(APIView):
	def get(self, request, format=None):
		try:
			listClient = Client.objects.all()
			serializer = ClientSerializer(listClient, many=True)
			return Response(serializer.data)
		except Client.DoesNotExist:
			raise Http404


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

class TermeParId(APIView):
	def get(self, request, termeid):
		try:
			return TermeFr.objects.get(pk=termeid)
		except TermeFr.DoesNotExist:
			raise Http404
	
	def get(self, request, termeid, format=None):
		termes = TermeFr.objects.get(pk=termeid)
		serializer = TermeFrSerializer(termes, many=False)
		return Response(serializer.data)

class TermeAnParId(APIView):
	def get(self, request, termeid):
		try:
			return TermeAn.objects.get(pk=termeid)
		except TermeAn.DoesNotExist:
			raise Http404
	
	def get(self, request, termeid, format=None):
		termesAn = TermeAn.objects.get(pk=termeid)
		serializer = TermeAnSerializer(termesAn, many=False)
		return Response(serializer.data)
