
from django.urls import path
from .views import (TripListView,
                    TripDetailView,
                    TripCreateView,
                    TripUpdateView,
                    TripDeleteView,
                    UserTripListView)
from . import views

urlpatterns = [
    path('', TripListView.as_view(), name='travel-home'),
    path('user/<str:username>', UserTripListView.as_view(), name='user-trips'),
    path('trip/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('trip/new/', TripCreateView.as_view(), name='trip-create'),
    path('trip/<int:pk>/update', TripUpdateView.as_view(), name='trip-update'),
    path('trip/<int:pk>/delete', TripDeleteView.as_view(), name='trip-delete'),
    path('about/', views.about, name='travel-about'),
]
