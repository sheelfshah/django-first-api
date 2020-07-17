from rest_framework import serializers
from api_app.models import TrialModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    models = serializers.PrimaryKeyRelatedField(
        many=True, queryset=TrialModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'trial_models']


class TrialModelSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = TrialModel
        fields = ['id', 'title', 'creator']
