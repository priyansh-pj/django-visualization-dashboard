
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render

def dashboard(request):
    return render(request,'dashboard.html')

def filter(request):
    return render(request,'filter.html')

def filter_view(request):
    url = request.build_absolute_uri()
    return render(request,'dashboard_filter.html',{'api':url.replace('filtered','api/filter')})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('dashboard.urls')),
    path('',dashboard, name='dashboard'),
    path('filtered/',filter_view ,name='filtered'),
    path('filter/',filter, name='filter'),
]
