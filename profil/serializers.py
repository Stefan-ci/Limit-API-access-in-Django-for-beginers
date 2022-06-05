from profil.models import Profile
from rest_framework.serializers import ModelSerializer, ReadOnlyField



class ProfileSerializer(ModelSerializer):
    username = ReadOnlyField(source='user.userame')
    class Meta:
        model = Profile
        fields = ['username', 'api_key', 'hashed_api_key', 'date']



