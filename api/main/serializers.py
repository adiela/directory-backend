from rest_framework import serializers
from django.contrib.auth import get_user_model


class BaseSerializer(serializers.HyperlinkedModelSerializer):
    pass
