from rest_framework import generics, permissions
from with_travel_in_mind_api.permissions import IsOwnerOrReadOnly
from commentlikes.models import CommentLike
from commentlikes.serializers import CommentLikeSerializer


class CommentLikeList(generics.ListCreateAPIView):
    """
    List comment likes.
    Make it possible to like a comment when logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment like. Delete it if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()
