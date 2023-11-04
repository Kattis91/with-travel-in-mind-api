from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Explorer
from .serializers import ExplorerSerializer

class ExplorerList(APIView):
    """
    List all explorers
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        explorers = Explorer.objects.all()
        serializer = ExplorerSerializer(explorers, many=True)
        return Response(serializer.data)
