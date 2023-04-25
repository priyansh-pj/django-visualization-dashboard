from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count, Func, Value ,Q
from django.db.models.functions import Lower,Concat
from .models import Data
from .serializers import *



# API functions here.
@api_view(['GET'])
def api_routes(requets):
    routes = [
        {'GET':'/api/data'},
        {'GET':'/intensity/'}
    ]
    return Response(routes)

    
@api_view(['GET'])
def filter(request):
    intensity = request.query_params.get('intensity-select')
    relevance = request.query_params.get('relevance-select')
    likelihood = request.query_params.get('likelihood-select')
    start_year = request.query_params.get('start-year-select')
    end_year = request.query_params.get('end-year-select')
    country = request.query_params.get('country-select')
    region = request.query_params.get('region-select')
    pestle = request.query_params.get('pestle-select')
    topic = request.query_params.get('topic-select')

    query = Q()

    if intensity:
        query &= Q(intensity=intensity)

    if relevance:
        query &= Q(relevance=relevance)

    if likelihood:
        query &= Q(likelihood=likelihood)

    if start_year:
        query &= Q(start_year=start_year)

    if end_year:
        query &= Q(end_year=end_year)

    if country:
        query &= Q(country=country)

    if region:
        query &= Q(region=region)

    if pestle:
        query &= Q(pestle=pestle)

    if topic:
        query &= Q(topic=topic)

    data = Data.objects.filter(query)

    serializers = DataSerializer(data,many=True)

    return Response(serializers.data)


@api_view(['GET'])
def visualization_data(request):
    data_counts = {}
    
    # Get intensity data
    intensity_data = Data.objects.values('intensity').annotate(count=Count('id'))
    serializer = IntensitySerializer(intensity_data, many=True)
    data_counts['intensity'] = serializer.data
    
    # Get likelihood data
    likelihood_data = Data.objects.values('likelihood').annotate(count=Count('id'))
    serializer = LikelihoodSerializer(likelihood_data, many=True)
    data_counts['likelihood'] = serializer.data
    
    # Get relevance data
    relevance_data = Data.objects.values('relevance').annotate(count=Count('id'))
    serializer = RelevanceSerializer(relevance_data, many=True)
    data_counts['relevance'] = serializer.data
    
    # Get country data
    country_data = Data.objects.exclude(country='').values('country').annotate(count=Count('id'))
    serializer = CountrySerializer(country_data, many=True)
    data_counts['country'] = serializer.data
    
    # Get start year data
    start_year_data = Data.objects.exclude(start_year=None).values('start_year').annotate(count=Count('id'))
    serializer = StartYearSerializer(start_year_data, many=True)
    data_counts['start_year'] = serializer.data
    
    # Get end year data
    end_year_data = Data.objects.exclude(end_year=None).values('end_year').annotate(count=Count('id'))
    serializer = EndYearSerializer(end_year_data, many=True)
    data_counts['end_year'] = serializer.data
    
    # Get topic data
    topic_data = Data.objects.exclude(topic='').annotate(topic_lower=Lower('topic')).values('topic_lower').annotate(count=Count('id')).annotate(topic=Concat(Value(''), Value(''), Lower('topic_lower'))).values('topic', 'count')
    serializer = TopicSerializer(topic_data, many=True)
    data_counts['topic'] = serializer.data
    
    # Get region data
    region_data = Data.objects.exclude(region='').annotate(region_lower=Lower('region')).values('region_lower').annotate(count=Count('id')).annotate(region=Concat(Value(''), Value(''), Lower('region_lower'))).values('region', 'count')
    serializer = RegionSerializer(region_data, many=True)
    data_counts['region'] = serializer.data
    
    # Get pestle data
    pestle_data = Data.objects.exclude(topic='').values('pestle').annotate(count=Count('id'))
    serializer = PestleSerializer(pestle_data, many=True)
    data_counts['pestle'] = serializer.data
    
    return Response(data_counts)