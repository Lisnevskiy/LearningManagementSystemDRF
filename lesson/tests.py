from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from lesson.models import Lesson
from users.models import User


class LessonTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='user@example.com',
            password='password'
        )

        cls.course = Course.objects.create(
            title='test course',
            description='test course description'
        )

        cls.lesson = Lesson.objects.create(
            title='test lesson',
            description='test lesson description',
            course=cls.course,
            owner=cls.user
        )

    def test_get_list(self):
        response = self.client.get(reverse('lesson:lessons'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "pk": 1,
                        "title": "test lesson",
                        "description": "test lesson description",
                        "image": None,
                        "video_url": None,
                        "course": 1,
                        "owner": 1
                    },

                ]
            }
        )

    def test_create_lesson(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'title': '2test lesson',
            'description': '2test lesson description',
            'video_url': 'https://www.youtube.com',
            'course': self.course.pk
        }

        response = self.client.post(
            reverse('lesson:lessons_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            2
        )

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'title': '2test lesson',
            'description': '2test lesson description',
            'video_url': 'https://www.youtube.com',
            'course': self.course.pk
        }

        response = self.client.put(
            reverse('lesson:lessons_update', args=[self.lesson.pk]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('lesson:lessons_delete', args=[self.lesson.pk])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Lesson.objects.all().count(),
            0
        )
