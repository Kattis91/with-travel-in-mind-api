from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    explorer_id = serializers.ReadOnlyField(source='owner.explorer.id')
    explorer_image = serializers.ReadOnlyField(source='owner.explorer.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'explorer_id', 
            'explorer_image', 'post', 'created_at', 
            'updated_at', 'comment'
        ]


class CommentDetailSerializer(CommentSerializer):
    
    post = serializers.ReadOnlyField(source='post.id')