from .models import Category, Business, OpeningHours, Product, Review
from api.main.serializers import BaseSerializer


class CategorySerializer(BaseSerializer):

    class Meta:
        model = Category
        fields = ['url', 'id', 'name', 'description']


class OpeningHoursSerializer(BaseSerializer):

    class Meta:
        model = OpeningHours
        fields = ['url', 'day', 'opening_time', 'closing_time']


class BusinessSerializer(BaseSerializer):
    opening_hours = OpeningHoursSerializer(many=True, read_only=False)

    class Meta:
        model = Business
        fields = ['url', 'id', 'name', 'category', 'description', 'location', 'location_description', 'phone_number',
                  'email', 'website', 'opening_hours']


class ProductSerializer(BaseSerializer):

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'description', 'business', 'price']


class ReviewSerializer(BaseSerializer):

    class Meta:
        model = Review
        fields = ['url', 'business', 'rating', 'text']
