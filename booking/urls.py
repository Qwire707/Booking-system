from django.urls import path
from .views import index, house_detail, booking_house

urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),
    path("houses/<int:pk>/", house_detail, name="house-detail"),
    path ("houses/<int:pk>/booking/", booking_house, name="booking-house")
]

