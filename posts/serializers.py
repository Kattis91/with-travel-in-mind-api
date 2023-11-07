from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from bookmarks.models import Bookmark


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    explorer_id = serializers.ReadOnlyField(source='owner.explorer.id')
    explorer_image = serializers.ReadOnlyField(
        source='owner.explorer.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    bookmark_id = serializers.SerializerMethodField()
    bookmarks_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Validate image size and dimensions
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']

    def get_like_id(self, obj):
        """
        Method to let us know if the current user
        has already liked a post
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_bookmark_id(self, obj):
        """
        Method to let us know if the current user
        has already bookmarked a post
        """
        user = self.context['request'].user
        if user.is_authenticated:
            bookmark = Bookmark.objects.filter(
                owner=user, post=obj
            ).first()
            return bookmark.id if bookmark else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'explorer_id',
            'explorer_image', 'created_at', 'updated_at',
            'title', 'description', 'image', 'country',
            'like_id', 'likes_count', 'bookmark_id',
            'bookmarks_count', 'comments_count'
        ]
