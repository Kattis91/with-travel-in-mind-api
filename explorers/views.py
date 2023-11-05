from django.db.models import Count
from rest_framework import generics, filters
from with_travel_in_mind_api.permissions import IsOwnerOrReadOnly
from .models import Explorer
from .serializers import ExplorerSerializer

class ExplorerList(generics.ListAPIView):
    """
    List all explorers
    No Create view (post method), as profile creation handled by django signals
    """
    queryset = Explorer.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        favourites_count=Count('owner__favorited', distinct=True),
        favoriting_count=Count('owner__favoriting', distinct=True)
    ).order_by('-created_at')
    serializer_class = ExplorerSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'favourites_count',
        'favoriting_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ExplorerDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Explorer.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
        favourites_count=Count('owner__favorited', distinct=True),
        favoriting_count=Count('owner__favoriting', distinct=True)
    ).order_by('-created_at')
    serializer_class = ExplorerSerializer
