from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Func, Value
from django.db.models.functions import Lower,Concat
from .models import Data
from .serializers import *

# Create your views here.
@api_view(['GET'])
def api_routes(requets):
    routes = [
        {'GET':'/api/data'},
        {'GET':'/intensity/'}
    ]
    return Response(routes)

@api_view(['GET'])
def data_list(request):
    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def intensity_visualization(request):
    data_counts = Data.objects.values('intensity').annotate(count=Count('id'))
    serializer = IntensitySerializer(data_counts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def likelihood_visualization(request):
    data_counts = Data.objects.values('likelihood').annotate(count=Count('id'))
    serializer = LikelihoodSerializer(data_counts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def relevance_visualization(request):
    data_counts = Data.objects.values('relevance').annotate(count=Count('id'))
    serializer = RelevanceSerializer(data_counts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def country_visualization(request):
    data_counts = Data.objects.values('country').annotate(count=Count('id'))
    serializer = CountrySerializer(data_counts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def start_year_visualization(request):
    data_counts = Data.objects.values('start_year').annotate(count=Count('id'))
    serializer = StartYearSerializer(data_counts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def end_year_visualization(request):
    data_counts = Data.objects.values('end_year').annotate(count=Count('id'))
    serializer = EndYearSerializer(data_counts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def topic_visualization(request):
    data_counts = Data.objects.annotate(region_lower=Lower('topic')).values('topic_lower').annotate(count=Count('id')).annotate(region=Concat(Value(''), Value(''), Lower('topic_lower'))).values('topic', 'count')
    serializer = TopicSerializer(data_counts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def region_visualization(request):
    # data_counts = Data.objects.values('region').annotate(count=Count('id'))
    data_counts = Data.objects.annotate(region_lower=Lower('region')).values('region_lower').annotate(count=Count('id')).annotate(region=Concat(Value(''), Value(''), Lower('region_lower'))).values('region', 'count')
    serializer = RegionSerializer(data_counts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pestle_visualization(request):
    data_counts = Data.objects.values('pestle').annotate(count=Count('id'))
    serializer = PestleSerializer(data_counts, many=True)
    return Response(serializer.data)