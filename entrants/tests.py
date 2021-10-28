from django.shortcuts import get_object_or_404
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from .models import Entrants
from objects.models import Objects


class EntrantsTests(APITestCase):
    factory = APIClient()

    def test_get_entrants(self):
        """
        Тест на получение всех поступающих через метод get
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
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        url = '/entrants/'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Entrants.objects.get().name, 'test')

    def test_get_entrant(self):
        """
        Тест на получение поступающего через метод get
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
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        url = f'/entrants/{new_entrants.id}/'
        response = self.factory.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Entrants.objects.get().name, 'test')

    def test_post_entrant(self):
        """
        Тест на проверку добавление поступающего через метод post
        """
        new_objects = Objects.objects.create(
            name='test2',
            mark=50,
        )
        new_objects.save()
        url = '/entrants/'
        data = {"name": "test2",
                "surname": "test2",
                "middlename": "test2",
                "birthday": '2001-02-02',
                "subject": new_objects.id,
                "mark": 60,
                }
        response = self.factory.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Entrants.objects.get().name, 'test2')

    def test_patch_entrant(self):
        """
        Тест на проверку обновление поступающего через метод patch
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
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        data = {"name": "test2",
                "surname": "test2",
                "middlename": "test2",
                "birthday": '2001-02-02',
                "mark": 60,
                }
        url = f'/entrants/{new_entrants.id}/'
        response = self.factory.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_object_or_404(Entrants, id=new_entrants.id).name, "test2")

    def test_delete_entrant(self):
        """
        Тест на проверку удаление поступающего методом delete
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
            subject=new_objects,
            mark=50,
        )
        new_entrants.save()
        url = f'/entrants/{new_entrants.id}/'
        response = self.factory.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
