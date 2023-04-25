
from django.urls import path
from . import views

urlpatterns = [
    path('routes/',views.api_routes),
    path('filter/',views.filter),    
    path('data/',views.visualization_data),
]
