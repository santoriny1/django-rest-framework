from django.shortcuts import render
from rest_framework import generics
from .models import Member, DriversLicense, Movie, MovieRental, Rental
from .serializers import DriverLicenseSerializer, MemberSerializer, MovieRentalSerializer, MovieSerializer, RentalSerializer

# Create your views here.
class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class DriverLicenseList(generics.ListCreateAPIView):
    queryset = DriversLicense.objects.all()
    serializer_class = DriverLicenseSerializer

class DriverLicenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DriversLicense.objects.all()
    serializer_class = DriverLicenseSerializer

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRentalList(generics.ListCreateAPIView):
    queryset = MovieRental.objects.all()
    serializer_class = MovieRentalSerializer

class MovieRentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieRental.objects.all()
    serializer_class = MovieRentalSerializer

class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

