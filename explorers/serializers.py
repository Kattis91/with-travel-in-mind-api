from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Explorer
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'region', 'dream_destination'
        ]
