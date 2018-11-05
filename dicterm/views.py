from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from django.template import loader
from terme.models import Client


# Create your views here.

class InfoView(APIView):
    renderer_classes = (JSONRenderer, )

    """List of routes for this API."""
    def get(self, request, format=None):
        output = {
            'info': 'GET /api/v1',
            "Liste des clients": 'GET /api/v1/clients',
            "Nouveau client": 'POST /api/v1/clients',
            "Detail client": 'GET /api/v1/clients/<id>',
            "MaJ client": 'PUT /api/v1/clients/<id>',
            "Efface client": 'DELETE /api/v1/clients/<id>',
            "Liste des domaines": 'GET /api/v1/domaines',
            "Nouveau domaine": 'POST /api/v1/domaines',
            "Detail domaine": 'GET /api/v1/domaines/<id>',
            "MaJ domaine": 'PUT /api/v1/domaines/<id>',
            "Efface domaine": 'DELETE /api/v1/domaines/<id>',
            "Liste des tags": 'GET /api/v1/tags',
            "Nouveau tag": 'POST /api/v1/tags',
            "Detail tag": 'GET /api/v1/tags/<id>',
            "MaJ tag": 'PUT /api/v1/tags/<id>',
            "Efface tag": 'DELETE /api/v1/tags/<id>',
            "Liste des termes": 'GET /api/v1/termes',
            "Nouveau terme": 'POST /api/v1/termes',
            "Detail terme": 'GET /api/v1/termes/<id>',
            "MaJ terme": 'PUT /api/v1/termes/<id>',
            "Efface terme": 'DELETE /api/v1/termes/<id>',
            "Liste des contexts": 'GET /api/v1/contexts',
            "Nouveau context": 'POST /api/v1/contexts',
            "Detail context": 'GET /api/v1/contexts/<id>',
            "MaJ context": 'PUT /api/v1/contexts/<id>',
            "Efface context": 'DELETE /api/v1/contexts/<id>'				
        }
        return Response(content)



def index(request):
    client_list = Client.objects.order_by('nom_client')
    contexte_list = Contexte.objects.order_by('contexte')
    template = loader.get_template('index.html')
    context = {
        'client_list': client_list,
        'contexte_list': contexte_list,
    }
    return HttpResponse(template.render(context, request))
