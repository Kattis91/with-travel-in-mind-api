from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Method to check if the authenticated user is the explorer's owner
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Explorer
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'region', 'dream_destination', 'is_owner'
        ]
