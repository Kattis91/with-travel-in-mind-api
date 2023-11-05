from rest_framework import serializers
from favourites.models import Favourite
from django.db import IntegrityError


class FavouriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    favorited_name = serializers.ReadOnlyField(source='favorited.username')

    class Meta:
        model = Favourite
        fields = [
            'id', 'owner', 'created_at', 'favorited', 'favorited_name'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
