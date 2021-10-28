from rest_framework.serializers import ModelSerializer
from .models import Objects


class ObjectsModelSerializer(ModelSerializer):
    class Meta:
        model = Objects
        fields = '__all__'
