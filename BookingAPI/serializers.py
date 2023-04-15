from rest_framework import serializers

from BookingAPI.models import Booking


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'title', 'author', 'price']
