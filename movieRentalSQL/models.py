from django.db import models
import uuid

# Create your models here.
class DriversLicense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    post_code = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    first_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    driver_license = models.ForeignKey(DriversLicense, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Rental(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    rental_date = models.DateField()
    rental_expiry = models.DateField()
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id')
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rental_cost = models.DecimalField(max_digits=6, decimal_places=2)
    year_of_release = models.PositiveSmallIntegerField()
    rental_duration = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class MovieRental(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)





