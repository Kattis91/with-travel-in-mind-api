from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
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


class ExplorerDetail(APIView):
    serializer_class = ExplorerSerializer
    def get_object(self, pk):
        try:
            explorer = Explorer.objects.get(pk=pk)
            return explorer
        except Explorer.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        explorer = self.get_object(pk)
        serializer = ExplorerSerializer(explorer)
        return Response(serializer.data)
    
    def put(self, request, pk):
        explorer = self.get_object(pk)
        serializer = ExplorerSerializer(explorer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
