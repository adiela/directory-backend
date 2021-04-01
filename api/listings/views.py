from .models import Category, Business, Product, Review, OpeningHours
from api.main.views import BaseViewSet
from .serializers import CategorySerializer, BusinessSerializer, OpeningHoursSerializer, ProductSerializer, ReviewSerializer


class CategoryViewSet(BaseViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BusinessViewSet(BaseViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class ProductViewSet(BaseViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OpeningHoursViewSet(BaseViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = OpeningHours.objects.all()
    serializer_class = OpeningHoursSerializer


class ReviewViewSet(BaseViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
