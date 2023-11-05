from rest_framework import generics
from with_travel_in_mind_api.permissions import IsOwnerOrReadOnly
from .models import Explorer
from .serializers import ExplorerSerializer

class ExplorerList(generics.ListAPIView):
    """
    List all explorers
    No Create view (post method), as profile creation handled by django signals
    """
    queryset = Explorer.objects.all()
    serializer_class = ExplorerSerializer


class ExplorerDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Explorer.objects.all()
    serializer_class = ExplorerSerializer
