from django.urls import path

from .views import CityListView, CityDetailView, HotelListView, HotelDetailView, ApartmentListView,ApartmentDetailView


urlpatterns = [
    path('', CityListView.as_view()),
    path('<int:pk>/', CityDetailView.as_view()),
    path('hotels/', HotelListView.as_view()),
    path('hotels/<int:pk>/', HotelDetailView.as_view()),
    path('apartments/', ApartmentListView.as_view()),
    path('apartments/<int:pk/', ApartmentDetailView.as_view()),
]