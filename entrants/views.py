from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import Entrants
from .serializers import EntrantsModelSerializer
from objects.models import Objects


class EntrantsModelViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer = EntrantsModelSerializer

    def list(self, request):
        """
        Метод для получение всех поступающих
        """
        entrants = Entrants.objects.all()
        serializer = EntrantsModelSerializer(entrants, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk: str or None = None):
        """
        Метод для получение поступающего
        """
        entrant = get_object_or_404(Entrants, id=pk)
        serializer = EntrantsModelSerializer(entrant)
        return Response(serializer.data)

    def post(self, request):
        """
        Метод для создание нового поступающего
        """
        data = request.data
        subject_id = get_object_or_404(Objects, id=data['subject'])
        new_entrant = Entrants.objects.create(
            name=data.get('name'),
            surname=data.get('surname'),
            middlename=data.get('middlename'),
            birthday=data.get('birthday'),
            subject=subject_id,
            mark=data.get('mark'),
        )
        new_entrant.save()

        serializer = EntrantsModelSerializer(new_entrant)
        return Response(serializer.data)

    def patch(self, request, pk: str or None = None):
        """
        Метод для изменения поступающего
        """
        entrant = get_object_or_404(Entrants, id=pk)
        data = request.data
        try:
            entrant.subject_id = get_object_or_404(Objects, id=data['subject'])
        except KeyError:
            pass
        for el in data:
            entrant.__dict__[el] = data[el]
        entrant.save()

        serializer = EntrantsModelSerializer(entrant)
        return Response(serializer.data)

    def delete(self, request, pk: str or None = None):
        """
        Метод для удаления поступающего
        """
        entrant = get_object_or_404(Entrants, id=pk)
        entrant.delete()

        serializer = EntrantsModelSerializer(entrant)
        return Response(serializer.data)
