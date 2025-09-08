# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    # Choices for country of origin
    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('DE', 'Germany'),
        ('JP', 'Japan'),
        ('KR', 'South Korea'),
        ('IT', 'Italy'),
        ('FR', 'France'),
        ('UK', 'United Kingdom'),
        ('SE', 'Sweden'),
        ('CN', 'China'),
        ('IN', 'India'),
        ('OTHER', 'Other'),
    ]

    #  Choices for status of car make
    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('ACTIVE', 'Active'),
        ('DISCONTINUED', 'Discontinued'),
        ('MERGED', 'Merged with another company'),
        ('BANKRUPT', 'Bankrupt'),
        ('ACQUIRED', 'Acquired by another company'),
        ('HIATUS', 'On hiatus'),
        ('DORMANT', 'Dormant/inactive'),
        ('ARCHIVED', 'Archived'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    founded_year = models.IntegerField(null=True,
                                       validators=[
                                           MaxValueValidator(2025),
                                           MinValueValidator(2015)
                                       ])
    defunct_year = models.IntegerField(null=True,
                                       validators=[
                                           MaxValueValidator(2025),
                                           MinValueValidator(2015)
                                       ])
    country = models.CharField(
        max_length=20,
        choices=COUNTRY_CHOICES,
        default='OTHER')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='DRAFT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE)  # Many-to-One relationship
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2025,
                               validators=[
                                   MaxValueValidator(2025),
                                   MinValueValidator(2015)
                               ])
    # Other fields as needed
    production_start_year = models.IntegerField(null=True,
                                                validators=[
                                                    MaxValueValidator(2025),
                                                    MinValueValidator(2015)
                                                ])
    production_end_year = models.IntegerField(null=True,
                                              validators=[
                                                  MaxValueValidator(2025),
                                                  MinValueValidator(2015)
                                              ])

    def __str__(self):
        return self.name  # Return the name as the string representation
