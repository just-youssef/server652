from rest_framework import serializers
from .models import *

class جنودSerializer(serializers.ModelSerializer):
    class Meta:
        model = جنود
        fields = '__all__'

class ضباطSerializer(serializers.ModelSerializer):
    class Meta:
        model = ضباط
        fields = '__all__'

class ضباط_صفSerializer(serializers.ModelSerializer):
    class Meta:
        model = ضباط_صف
        fields = '__all__'