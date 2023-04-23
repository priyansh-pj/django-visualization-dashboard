
from django.urls import path
from . import views

urlpatterns = [
    path('routes/',views.api_routes),
    path('get_all_data/',views.data_list),
    path('intensity/',views.intensity_visualization),
    path('likelihood/',views.likelihood_visualization),
    path('relevance/',views.relevance_visualization),
    path('country/',views.country_visualization),
    path('start_year/',views.start_year_visualization),
    path('end_year/',views.end_year_visualization),
    path('topic/',views.topic_visualization),
    path('region/',views.region_visualization),
    path('pestle/',views.pestle_visualization),

]
