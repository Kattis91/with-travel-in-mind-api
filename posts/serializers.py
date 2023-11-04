from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    explorer_id = serializers.ReadOnlyField(source='owner.explorer.id')
    explorer_image = serializers.ReadOnlyField(source='owner.explorer.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'explorer_id',
            'explorer_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'country'
        ]