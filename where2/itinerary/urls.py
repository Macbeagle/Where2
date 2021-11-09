from django.urls import path, include
from itinerary import views
from itinerary.views import HomeView, itinerary_view, resturant_view, activity_view

urlpatterns = [
    path('', HomeView.as_view()),
    path('itinerary/', views.itinerary_view, name='itinerary'),
    path('resturants/', views.resturant_view, name='resturants'),
    path('activities/', views.activity_view, name='activities')
]
