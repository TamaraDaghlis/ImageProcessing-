from django.urls import path
from api import views

urlpatterns = [
    path('api/searchCar', views.searchCar, name="search-car")
]