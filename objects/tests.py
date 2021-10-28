from django.shortcuts import get_object_or_404
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .models import Objects
from directions.models import Directions
from entrants.models import Entrants


class ObjectsTests(APITestCase):
    factory = APIClient()

    def test_get_objects(self):
        """
        Тест на получение всех предметов через метод get
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        url = '/objects/'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Objects.objects.get().name, 'test2')

    def test_get_object(self):
        """
        Тест на получение предмета через метод get
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        url = f'/objects/{new_objects.id}/'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Objects.objects.get().name, 'test2')

    def test_post_object(self):
        """
        Тест на проверку добавление предмета через метод post
        """
        url = '/objects/'
        data = {"name": "test", "mark": 40}
        response = self.factory.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Objects.objects.get().name, 'test')

    def test_patch_object(self):
        """
        Тест на проверку обновление предмета через метод patch
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        data = {"mark": 80}
        url = f'/objects/{new_objects.id}/'
        response = self.factory.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_object_or_404(Objects, id=new_objects.id).mark, 80)

    def test_delete_object(self):
        """
        Тест на проверку удаление объектов методом delete
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        url = f'/objects/{new_objects.id}/'
        response = self.factory.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_object_direction(self):
        """
        Тест на получение всех предметов определенного направления
        """
        new_objects = Objects.objects.create(
            name='test1',
            mark=50,
        )
        new_objects.save()
        new_objects2 = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects2.save()
        new_entrants = Entrants.objects.create(
            name='test',
            surname='test',
            middlename='test',
            birthday='2000-01-01',
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        new_direction = Directions.objects.create(
            name='test',
            object=new_objects2,
            entrant=new_entrants,
        )
        url = f'/objects_direction/{new_direction.id}'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'test2')
