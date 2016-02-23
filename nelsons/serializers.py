from rest_framework import serializers

from .models import Nelson

class NelsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nelson
        fields = ('name', 'latitude', 'longitude', 'position', 'last_activity')
        read_only_fields = ('name', 'latitude', 'longitude', 'last_activity')
