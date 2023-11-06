from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    explorer_id = serializers.ReadOnlyField(source='explorer.id')
    explorer_image = serializers.ReadOnlyField(source='explorer.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'explorer_id', 'explorer_image'
        )