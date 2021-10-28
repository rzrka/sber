from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Directions
from .serializers import DirectionsModelSerializer
from entrants.models import Entrants
from objects.models import Objects


class DirectionsModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer = DirectionsModelSerializer

    def list(self, request):
        """
        метод для получения всех направлений
        """
        directions = Directions.objects.all()
        serializer = DirectionsModelSerializer(directions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk: str or None = None):
        """
        метод для получения одного направления
        """
        directions = get_object_or_404(Directions, id=pk)
        serializer = DirectionsModelSerializer(directions)
        return Response(serializer.data)

    def post(self, request):
        """
        метод для создания направления
        """
        data = request.data
        entrant = get_object_or_404(Entrants, id=data['entrant'])
        object = get_object_or_404(Objects, id=data['object'])
        new_direction = Directions.objects.create(
            name=data['name'],
            entrant=entrant,
            object=object,
        )
        new_direction.save()

        serializer = DirectionsModelSerializer(new_direction)
        return Response(serializer.data)

    def patch(self, request, pk: str or None = None):
        """
        Метод для изменения одного или несколько полей направления
        """
        direction = get_object_or_404(Directions, id=pk)
        data = request.data
        try:
            name = data['name']
            direction.name = name
        except KeyError:
            pass
        try:
            entrant_id = get_object_or_404(Entrants, id=data['entrant'])
            direction.entrant = entrant_id
        except KeyError:
            pass
        try:
            object_id = get_object_or_404(Objects, id=data['object'])
            direction.object = object_id
        except KeyError:
            pass

        direction.save()

        serializer = DirectionsModelSerializer(direction)
        return Response(serializer.data)

    def delete(self, request, pk: str or None = None):
        """
        Метод для удаления направления
        """
        direction = get_object_or_404(Directions, id=pk)
        direction.delete()

        serializer = DirectionsModelSerializer(direction)
        return Response(serializer.data)
