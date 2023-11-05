from rest_framework import generics, permissions
from with_travel_in_mind_api.permissions import IsOwnerOrReadOnly
from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer


class BookmarkList(generics.ListCreateAPIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookmarkDetail(generics.RetrieveDestroyAPIView):
  
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()