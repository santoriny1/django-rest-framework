from rest_framework import serializers
from .models import DriversLicense, Member, Movie, MovieRental, Rental

class DriverLicenseSerializer(serializers.ModelSerializer):
    class Meta: 
        model = DriversLicense
        fields = ('id', 'first_name', 'last_name', 'address', 'post_code', 'date_of_birth', 'expiry_date', 'created_at')
        read_only_fields = ('created_at',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Movie
        fields = ('id', 'name', 'director', 'rental_cost', 'year_of_release', 'rental_duration', 'created_at')
        read_only_fields = ('created_at',)

class MemberSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Member
        fields = ('id', 'first_name', 'address', 'phone', 'email', 'driver_license', 'created_at')
        read_only_fields = ('created_at',)

class MovieRentalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MovieRental
        fields = ('id', 'rental', 'movie', 'created_at')
        read_only_fields = ('created_at',)

class RentalSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rental
        fields = ('id', 'member', 'rental_date', 'rental_expiry', 'total_cost', 'created_at')
        read_only_fields = ('created_at',)