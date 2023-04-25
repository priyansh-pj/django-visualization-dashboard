from rest_framework import serializers
from .models import Data


class IntensitySerializer(serializers.Serializer):
    intensity_id = serializers.SerializerMethodField()
    intensity = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('intensity_id', 'intensity', 'count')

    def get_intensity(self, obj):
        intensity = obj['intensity']
        if intensity is None:
            intensity = 0
        intensity = f'intensity ({str(intensity)})' 
        return intensity
    def get_intensity_id(self, obj):
        intensity = obj['intensity']
        if intensity is None:
            intensity = 0
        intensity = f'{str(intensity)}' 
        return intensity
    
class LikelihoodSerializer(serializers.Serializer):
    likelihood_id = serializers.SerializerMethodField()
    likelihood = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('likelihood_id', 'likelihood', 'count')

    def get_likelihood_id(self, obj):
        likelihood = obj['likelihood']
        if likelihood is None:
            likelihood = 0
        likelihood = f'{str(likelihood)}' 
        return likelihood

    def get_likelihood(self, obj):
        likelihood = obj['likelihood']
        if likelihood is None:
            likelihood = 0
        likelihood = f'likelihood ({str(likelihood)})' 
        return likelihood

class RelevanceSerializer(serializers.Serializer):
    relevance_id = serializers.SerializerMethodField()
    relevance = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('relevance_id', 'relevance', 'count')

    def get_relevance(self, obj):
        relevance = obj['relevance']
        if relevance is None:
            relevance = 0
        relevance = f'relevance ({str(relevance)})' 
        
        return relevance
    
    def get_relevance_id(self, obj):
        relevance = obj['relevance']
        if relevance is None:
            relevance = 0
        relevance = f'{str(relevance)}' 
        return relevance

class CountrySerializer(serializers.Serializer):
    country = serializers.SerializerMethodField()
    count = serializers.IntegerField()
    class Meta:
        fields = ('country', 'count')

    def get_country(self, obj):
        country = obj['country']
        if country is '':
            country = 'Invalid Country'
        return country

class StartYearSerializer(serializers.Serializer):
    start_year = serializers.SerializerMethodField()
    count = serializers.IntegerField()
    class Meta:
        fields = ('start_year', 'count')

    def get_start_year(self, obj):
        year = obj['start_year']
        if year is None:
            year =  'Invalid Year'
        return year
    
class EndYearSerializer(serializers.Serializer):
    end_year = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('end_year', 'count')

    def get_end_year(self, obj):
        year = obj['end_year']
        if year is None:
            year =  'Invalid Year'
        return year


class TopicSerializer(serializers.Serializer):
    topic = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('topic', 'count')

    def get_topic(self, obj):
        topic = obj['topic'].title()
        if topic is '':
            topic =  'Invalid Topic'
        return topic

class RegionSerializer(serializers.Serializer):
    region = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('region', 'count')

    def get_region(self, obj):
        region = obj['region'].title()
        if region is '':
            region =  'Invalid Region'
        return region

class PestleSerializer(serializers.Serializer):
    pestle = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('pestle', 'count')

    def get_pestle(self, obj):
        pestle = obj['pestle'].title()
        if pestle is '':
            pestle =  'Invalid Pestle'
        return pestle

class SourceSerializer(serializers.Serializer):
    source = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('source', 'count')

    def get_source(self, obj):
        source = obj['source'].title()
        if source is '':
            source =  'Invalid Source'
        return source

class SectorSerializer(serializers.Serializer):
    sector = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    class Meta:
        fields = ('sector', 'count')

    def get_sector(self, obj):
        sector = obj['sector'].title()
        if sector is '':
            sector =  'Invalid sector'
        return sector