from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"

class IntensitySerializer(serializers.Serializer):
    intensity = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('intensity', 'count')

    def get_intensity(self, obj):
        intensity = obj['intensity']
        if intensity is None:
            intensity = 0
        intensity = f'intensity ({str(intensity)})' 
        return intensity
    
class LikelihoodSerializer(serializers.Serializer):
    likelihood = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('likelihood', 'count')

    def get_likelihood(self, obj):
        likelihood = obj['likelihood']
        if likelihood is None:
            likelihood = 0
        likelihood = f'likelihood ({str(likelihood)})' 
        return likelihood

class RelevanceSerializer(serializers.Serializer):
    relevance = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('relevance', 'count')

    def get_relevance(self, obj):
        relevance = obj['relevance']
        if relevance is None:
            relevance = 0
        relevance = f'relevance ({str(relevance)})' 
        
        return relevance

class CountrySerializer(serializers.Serializer):
    country = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('country', 'count')

    def get_country(self, obj):
        country = obj['country']
        if country is None:
            country = 0
        return country

class StartYearSerializer(serializers.Serializer):
    start_year = serializers.SerializerMethodField()
    count = serializers.IntegerField()


    class Meta:
        fields = ('start_year', 'count')

    def get_start_year(self, obj):
        year = obj['start_year']
        if year is None:
            year = 0
        return year
    
class EndYearSerializer(serializers.Serializer):
    end_year = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('end_year', 'count')

    def get_end_year(self, obj):
        year = obj['end_year']
        if year is None:
            year = 0
        return year


class TopicSerializer(serializers.Serializer):
    topic = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('topic', 'count')

    def get_topic(self, obj):
        topic = obj['topic'].title()
        if topic is None:
            topic = 0
        return topic

class RegionSerializer(serializers.Serializer):
    region = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('region', 'count')

    def get_region(self, obj):
        region = obj['region'].title()
        if region is None:
            region = 0
        return region

class PestleSerializer(serializers.Serializer):
    pestle = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('pestle', 'count')

    def get_pestle(self, obj):
        pestle = obj['pestle'].title()
        if pestle is None:
            pestle = 0
        return pestle