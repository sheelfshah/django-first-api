from rest_framework import serializers
from api_app.models import TrialModel
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    trial_models = serializers.HyperlinkedRelatedField(
        many=True, view_name="model_detail", read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='user_detail', read_only=True)
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email',
                  'password', 'password2', 'trial_models']
        extra_kwargs = {
            'password': {'write_only': True, 'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        if "password2" in validated_data:
            del validated_data["password2"]
        if "password" in validated_data:
            del validated_data["password"]
        return User.objects.create(**validated_data)

    def save(self):
        user = super().save()
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            user.delete()
            raise serializers.ValidationError(
                {'password': 'Passwords must match'})
        user.set_password(password)
        user.save()
        return user


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
