from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'registration_number') # You can include other read-only fields
        read_only_fields = ('id', 'registration_number')
    