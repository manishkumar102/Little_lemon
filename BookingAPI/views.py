from django.shortcuts import render
from rest_framework import generics

from BookingAPI.models import Booking
from BookingAPI.serializers import BookSerializer


# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer


class SingleBookView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer
