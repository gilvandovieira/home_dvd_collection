from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Ator, Filme

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = ['id','nome', 'filmes']

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['id', 'nome', 'ano', 'atores']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']