from rest_framework import serializers
from commentlikes.models import CommentLike
from django.db import IntegrityError


class CommentLikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLike
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        """
        A method to prevent users from
        creating duplicate comment likes
        """
        comment = validated_data.get('comment')

        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })