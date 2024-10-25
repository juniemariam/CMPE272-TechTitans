from rest_framework import serializers
from .models import CarList

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = ('id', 'car_title', 'description', 'created_on')

