from rest_framework.serializers import ModelSerializer
from .models import Entrants


class EntrantsModelSerializer(ModelSerializer):
    class Meta:
        model = Entrants
        fields = '__all__'
