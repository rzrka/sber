from rest_framework.serializers import ModelSerializer
from .models import Directions


class DirectionsModelSerializer(ModelSerializer):
    class Meta:
        model = Directions
        fields = '__all__'
