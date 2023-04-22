
from django.urls import path
from . import views

urlpatterns = [
    path('routes/',views.api_routes),
    path('get_all_data/',views.data_list),
]
