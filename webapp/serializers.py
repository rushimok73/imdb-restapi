from rest_framework import serializers
from .models import moviedata

class movieSerializer(serializers.ModelSerializer):

    class Meta:
        model = moviedata
        fields = '__all__'
