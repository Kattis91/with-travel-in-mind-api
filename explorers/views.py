from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Explorer

class ExplorerList(APIView):
    """
    List all eplorers
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        explorers = Explorer.objects.all()
      
