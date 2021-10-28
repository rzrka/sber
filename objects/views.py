from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Objects
from .serializers import ObjectsModelSerializer
from directions.models import Directions


class ObjectsDirectionModelViewSet(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer = ObjectsModelSerializer

    def get(self, request, pk: str or None = None):
        """
        Метод для получение всех предметов у определенного направления
        """
        name_direct = get_object_or_404(Directions, id=pk).name
        objects = list(map(lambda x: get_object_or_404(Objects, pk=x.object_id),
                           Directions.objects.filter(name__contains=name_direct)))

        serializer = ObjectsModelSerializer(objects, many=True)
        return Response(serializer.data)


class ObjectsModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer = ObjectsModelSerializer

    def list(self, request):
        """
        Метод для получения всех предметов
        """
        objects = Objects.objects.all()
        serializer = ObjectsModelSerializer(objects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk: str or None = None):
        """
        Метод для получения предмета
        """
        objects = get_object_or_404(Objects, id=pk)
        serializer = ObjectsModelSerializer(objects)
        return Response(serializer.data)

    def post(self, request):
        """
        Метод для создание предмета
        """
        data = request.data
        new_objects = Objects.objects.create(
            name=data['name'],
            mark=data.get('mark'),
        )
        new_objects.save()

        serializer = ObjectsModelSerializer(new_objects)
        return Response(serializer.data)

    def patch(self, request, pk: str or None = None):
        """
        Метод для изменения предмета
        """
        objects = get_object_or_404(Objects, id=pk)
        data = request.data
        for el in data:
            objects.__dict__[el] = data[el]
        objects.save()

        serializer = ObjectsModelSerializer(objects)
        return Response(serializer.data)

    def delete(self, request, pk: str or None = None):
        """
        Метод для удаления предмета
        """
        objects = get_object_or_404(Objects, id=pk)
        objects.delete()

        serializer = ObjectsModelSerializer(objects)
        return Response(serializer.data)
