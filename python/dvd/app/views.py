from rest_framework import generics,permissions
from django.contrib.auth.models import User
from .models import Ator, Filme
from .serializers import AtorSerializer, FilmeSerializer, UserSerializer

class AtorList(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FilmeList(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer