from api_app.serializers import TrialModelSerializer, UserSerializer
from api_app.models import TrialModel
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from api_app.permissions import IsCreatorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    if request.method == "GET":
        return Response({
            'users': reverse('user_list', request=request, format=format),
            'snippets': reverse('model_list', request=request, format=format)
        })


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
        serializer.save(creator=self.request.user)


class TrialModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrialModel.objects.all()
    serializer_class = TrialModelSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCreatorOrReadOnly]
