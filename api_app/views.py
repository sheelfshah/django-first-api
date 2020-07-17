from api_app.serializers import TrialModelSerializer, UserSerializer
from api_app.models import TrialModel
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TrialModelList(generics.ListCreateAPIView):
    queryset = TrialModel.objects.all()
    serializer_class = TrialModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TrialModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrialModel.objects.all()
    serializer_class = TrialModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
