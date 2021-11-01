from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from . import views


urlpatterns = [
    path('cinema/<int:pk>/', views.CinemaRetrieveAPIView.as_view()),
    path('city/create/', views.CityCreateAPIView.as_view()),    # Запись города в БД
    path('city/all/', views.CityListView.as_view()),    # Вывод всех городов в которых есть кинотеатр
    path('city/detail/<int:pk>/', views.CityDetailView.as_view()),   # Подробности о городе
    path('city/cinema/', views.CinemaRetrieveAPIView.as_view()),
    #path('city/<int:pk>/cinema/<int:pk>/films_today/', ...),
    # url('city/<int:pk>/cinema/', views.TestAPIView.as_view()),
    #path('',)
]
