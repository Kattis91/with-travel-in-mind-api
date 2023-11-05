from rest_framework import serializers
from bookmarks.models import Bookmark
from django.db import IntegrityError


class BookmarkSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bookmark
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        
        post = validated_data.get('post')

        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
