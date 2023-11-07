from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the CurrentUser.
    Extends the UserDetailsSerializer from 'dj_rest_auth'
    to include 'explorer_id' and 'explorer_image' fields.
    """
    explorer_id = serializers.ReadOnlyField(source='explorer.id')
    explorer_image = serializers.ReadOnlyField(source='explorer.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'explorer_id', 'explorer_image'
        )
