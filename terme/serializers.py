from rest_framework import serializers
from terme.models import Client, Domaine, Tag, Terme, Context

class ClientSerializer(serializers.ModelSerializer):
    """Serializer pour la classe Client."""

    class Meta:
        model = Client
        fields = ('id', 'nom_client')

class DomaineSerializer(serializers.ModelSerializer):
    """Serializer pour la classe Domaine."""

    class Meta:
        model = Domaine
        fields = ('id', 'nom_domaine','client')

class TagSerializer(serializers.ModelSerializer):
    """Serializer pour la classe Tag."""

    class Meta:
        model = Tag
        fields = ('id', 'nom_tag')

class TermeSerializer(serializers.ModelSerializer):
    """Serializer pour la classe Terme."""

    class Meta:
        model = Terme
        fields = ('id', 'terme_fr','terme_an','definition','domaine','tag')

class ContextSerializer(serializers.ModelSerializer):
    """Serializer pour la classe Tag."""

    class Meta:
        model = Context
        fields = ('id', 'source','context')
