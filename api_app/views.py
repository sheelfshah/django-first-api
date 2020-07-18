from api_app.serializers import TrialModelSerializer, UserSerializer
from api_app.models import TrialModel
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from api_app.permissions import IsCreatorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth import login
# from django.contrib.auth import authenticate, logout
# from django.shortcuts import render, get_object_or_404, redirect


@api_view(['GET'])
def api_root(request, format=None):
    if request.method == "GET":
        return Response({
            'users': reverse('user_list', request=request, format=format),
            'snippets': reverse('model_list', request=request, format=format)
        })


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class TrialModelList(generics.ListCreateAPIView):
    queryset = TrialModel.objects.all()
    serializer_class = TrialModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TrialModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrialModel.objects.all()
    serializer_class = TrialModelSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
