from django.shortcuts import get_object_or_404
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from entrants.models import Entrants
from objects.models import Objects
from .models import Directions


class DirectionsTests(APITestCase):
    factory = APIClient()

    def test_get_directions(self):
        """
        Тест на получение всех направлений через метод get
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        new_entrants = Entrants.objects.create(
            name='test',
            surname='test',
            middlename='test',
            birthday='2000-01-01',
            pass_number=1234,
            pass_series=56723,
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        new_directions = Directions.objects.create(
            name='test',
            entrant=new_entrants,
            object=new_objects,
        )
        new_directions.save()
        url = '/directions/'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Directions.objects.get().name, 'test')

    def test_get_direction(self):
        """
        Тест на получение направления через метод get
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        new_entrants = Entrants.objects.create(
            name='test',
            surname='test',
            middlename='test',
            birthday='2000-01-01',
            pass_number=1234,
            pass_series=56723,
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        new_directions = Directions.objects.create(
            name='test',
            entrant=new_entrants,
            object=new_objects,
        )
        new_directions.save()
        url = f'/directions/{new_directions.id}/'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Directions.objects.get().name, 'test')

    def test_post_direction(self):
        """
        Тест на проверку добавление направления через метод post
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        new_entrants = Entrants.objects.create(
            name='test',
            surname='test',
            middlename='test',
            birthday='2000-01-01',
            pass_number=1234,
            pass_series=56723,
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        url = '/directions/'
        data = {"name": "test2",
                "object": new_objects.id,
                "entrant": new_entrants.id,
                }
        response = self.factory.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Directions.objects.get().name, 'test2')

    def test_patch_direction(self):
        """
        Тест на проверку обновление направления через метод patch
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        new_entrants = Entrants.objects.create(
            name='test',
            surname='test',
            middlename='test',
            birthday='2000-01-01',
            pass_number=1234,
            pass_series=56723,
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        new_directions = Directions.objects.create(
            name='test',
            entrant=new_entrants,
            object=new_objects,
        )
        new_directions.save()
        data = {"name": "test2",
                "object": new_objects.id,
                }
        url = f'/directions/{new_directions.id}/'
        response = self.factory.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_object_or_404(Directions, id=new_directions.id).name, "test2")

    def test_delete_direction(self):
        """
        Тест на проверку удаление направления методом delete
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        new_entrants = Entrants.objects.create(
            name='test',
            surname='test',
            middlename='test',
            birthday='2000-01-01',
            pass_number=1234,
            pass_series=56723,
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        new_directions = Directions.objects.create(
            name='test',
            entrant=new_entrants,
            object=new_objects,
        )
        new_directions.save()
        url = f'/directions/{new_directions.id}/'
        response = self.factory.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
