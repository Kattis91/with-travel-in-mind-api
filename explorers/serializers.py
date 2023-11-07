from rest_framework import serializers
from .models import Explorer
from followers.models import Follower
from favourites.models import Favourite


class ExplorerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Explorer model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    favoriting_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    favourites_count = serializers.ReadOnlyField()
    favoriting_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Method to check if the authenticated user is the explorer's owner
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Method to display the following_id (the same id as
        the newly created Follower instance) in order to know
        which Follower instance to delete when unfollowing
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    def get_favoriting_id(self, obj):
        """
        Method to display the favoriting_id (the same id as
        the newly created Favourite instance) in order to know
        which Favourite instance to delete when 'unfavoriting'
        """
        user = self.context['request'].user
        if user.is_authenticated:
            favoriting = Favourite.objects.filter(
                owner=user, favorited=obj.owner
            ).first()
            return favoriting.id if favoriting else None
        return None

    class Meta:
        model = Explorer
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'region_you_would_like_to_explore',
            'dream_destination', 'is_owner', 'following_id',
            'favoriting_id', 'posts_count', 'followers_count',
            'following_count', 'favourites_count', 'favoriting_count',
        ]
