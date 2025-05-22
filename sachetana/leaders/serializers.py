from rest_framework import serializers
from .models import Leader

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class LeaderSerializer(serializers.ModelSerializer):
    promises = PromiseSerializer(many=True, read_only=True)

    class Meta:
        model = Leader
        fields = '__all__'
