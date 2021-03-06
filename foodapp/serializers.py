from rest_framework import serializers
from .models import Foods

class FoodSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Foods
        fields = ['id', 'name', 'rate', 'typ', 'image']
        