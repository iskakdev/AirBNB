from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


class Country(models.Model):
    country_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.city_name


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(99)], null=True, blank=True)
    phone_number = PhoneNumberField()
    StatusRole = (
        ('guest', 'guest'),
        ('host', 'host')
    )
    user_role = models.CharField(max_length=32, choices=StatusRole, default='guest')
    avatar = models.ImageField(upload_to='avatar_image/', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Rules(models.Model):
    RulesChoices = (
        ('no_smoking', 'no_smoking'),
        ('pets_allowed', 'pets_allowed'),
        ('etc', 'etc')
    )
    rules = models.CharField(max_length=64, choices=RulesChoices)

    def __str__(self):
        return self.rules


class Property(models.Model):
    property_name = models.CharField(max_length=64)
    description = models.TextField()
    price_per_night = models.PositiveIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    PropertyTypeChoices = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('studio', 'studio')
    )
    property_type = models.CharField(max_length=32, choices=PropertyTypeChoices)
    rules = models.ManyToManyField(Rules)
    property_stars = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    max_guests = models.PositiveSmallIntegerField()
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='properties')
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.property_name}'

    def get_avg_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum(i.rating for i in reviews) / reviews.count(), 1)
        return 0

    def get_count_people(self):
        reviews = self.reviews.all()
        return reviews.count()


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_image')
    property_image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f'{self.property}, {self.property_image}'


class Booking(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    StatusChoiceRole = (
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('cancelled', 'cancelled')
    )
    status = models.CharField(max_length=32, choices=StatusChoiceRole)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.property}'


class Review(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    guests = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.guests}'
