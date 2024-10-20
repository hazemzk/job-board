from rest_framework import serializers
from .models import * 

# Serializers define the API representation.
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'