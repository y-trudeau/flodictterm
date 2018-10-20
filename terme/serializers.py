from rest_framework import serializers
from terme.models import Client, Domaine, Tag, TermeAn, TermeFr, Contexte, RelTermeAnFr

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

class TermeAnSerializer(serializers.ModelSerializer):
    """Serializer pour la classe TermeAn."""

    class Meta:
        model = TermeAn
        fields = ('id', 'terme','definition','note','domaine')

class TermeFrSerializer(serializers.ModelSerializer):
    """Serializer pour la classe TermeFr."""

    class Meta:
        model = TermeAn
        fields = ('id', 'terme','definition','note','contexte')

class RelTermeAnFrSerializer(serializers.ModelSerializer):
    """Serializer pour la classe RelTermAnFr."""

    class Meta:
        model = RelTermeAnFr
        fields = ('id', 'termeAn','contexte','termeFr')

class ContexteSerializer(serializers.ModelSerializer):
    """Serializer pour la classe Tag."""

    class Meta:
        model = Contexte
        fields = ('id', 'source','contexte','note')
