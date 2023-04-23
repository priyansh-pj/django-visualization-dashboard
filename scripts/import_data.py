from dashboard.models import Data
from datetime import datetime
import json 

with open('jsondata.json') as f:
    data = json.load(f)

for item in data:
    end_year = item['end_year'] if item['end_year'] else None
    intensity = item['intensity'] if item['intensity'] else None
    impact = item['impact'] if item['impact'] else None
    start_year = item['start_year'] if item['start_year'] else None
    likelihood = item['likelihood'] if item['likelihood'] else None
    added = (datetime.strptime(item['added'],  '%B, %d %Y %H:%M:%S')).strftime('%Y-%m-%d %H:%M:%S') if item['added'] else None
    published = (datetime.strptime(item['published'],  '%B, %d %Y %H:%M:%S')).strftime('%Y-%m-%d %H:%M:%S') if item['published'] else None
    relevance = item['relevance'] if item['relevance'] else None
    obj = Data(end_year=end_year, intensity=intensity, sector=item['sector'], topic=item['topic'], insight=item['insight'], url=item['url'], region=item['region'], start_year=start_year, impact=impact, added=added, published=published, country=item['country'], relevance=relevance, pestle=item['pestle'], source=item['source'], title=item['title'], likelihood=likelihood)
    obj.save()