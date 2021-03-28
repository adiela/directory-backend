from django.contrib import admin
from api.listings.models import Category, Business, OpeningHours, Product, Review


admin.site.register(Category)
admin.site.register(Business)
admin.site.register(OpeningHours)
admin.site.register(Product)
admin.site.register(Review)
