from rest_framework import serializers
from api_app.models import TrialModel
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    trial_models = serializers.HyperlinkedRelatedField(
        many=True, view_name="model_detail", read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='user_detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'trial_models']


class TrialModelSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    # both the following methods to get creator_url work
    # creator_url = UserSerializer(read_only=True).fields['url']
    creator_url = serializers.HyperlinkedRelatedField(
        many=False, view_name="user_detail",
        queryset=User.objects.all(), source='creator')
    url = serializers.HyperlinkedIdentityField(
        view_name='model_detail', read_only=True)

    class Meta:
        model = TrialModel
        fields = ['url', 'id', 'title', 'creator', 'creator_url']
