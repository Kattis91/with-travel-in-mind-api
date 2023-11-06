from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from with_travel_in_mind_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """ 
    Displays a list of all posts 
    Make it possible to create posts when logged in
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        bookmarks_count=Count('bookmarks', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # posts by users a user is following
        'owner__followed__owner__explorer',
        # posts a user liked
        'likes__owner__explorer',
        # posts a user bookmarked
        'bookmarks__owner__explorer',
        # posts owned by a user
        'owner__explorer',
    ]
    search_fields = [
        'owner__username',
        'title',
        'country',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'bookmarks_count',
        'likes__created_at',
        'bookmarks__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update/delete a post if you're the owner.
    """    
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
        bookmarks_count=Count('bookmarks', distinct=True)
    ).order_by('-created_at')