from api.main.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings


class Category(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=256)

    class Meta:
        db_table = 'category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Business(BaseModel):
    name = models.CharField(max_length=75)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    location = models.PointField()
    location_description = models.CharField(max_length=120)
    phone_number = PhoneNumberField()
    email = models.EmailField()
    website = models.URLField()

    class Meta:
        db_table = 'business'
        verbose_name_plural = "Businesses"

    def __str__(self):
        return f"{self.id} {self.name}"


class OpeningHours(BaseModel):
    business = models.ForeignKey(Business, related_name="opening_hours", on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(validators=[MaxValueValidator(6), ])
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    class Meta:
        db_table = 'opening_hours'
        verbose_name_plural = "Opening Hours"


class Product(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=11)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return f"{self.business.name} {self.name} product"


class Review(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, null=True)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()

    class Meta:
        db_table = 'review'


class BusinessAdmin(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
