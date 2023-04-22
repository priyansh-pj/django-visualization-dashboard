from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Data
from .serializers import DataSerializer

# Create your views here.
@api_view(['GET'])
def api_routes(requets):
    routes = [
        {'GET':'/api/data'}
    ]
    return Response(routes)

@api_view(['GET'])
def data_list(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)