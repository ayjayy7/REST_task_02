from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView,DestroyAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, DetailSerializer, UpdateSerializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


class BookingsDetail(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = DetailSerializer
	lookup_fiels = 'id'
	lookup_url_kwarg = 'detail_id'


class BookingsUpdate(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateSerializer
	lookup_fiels = 'id'
	lookup_url_kwarg = 'detail_id'


class BookingsDelete(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_fiels = 'id'
	lookup_url_kwarg = 'detail_id'
