from rest_framework import serializers
from .models import *

class جنودSerializer(serializers.ModelSerializer):
    class Meta:
        model = gnod
        fields = '__all__'

class ضباطSerializer(serializers.ModelSerializer):
    class Meta:
        model = dobat
        fields = '__all__'

class ضباط_صفSerializer(serializers.ModelSerializer):
    class Meta:
        model = dobat_saf
        fields = '__all__'