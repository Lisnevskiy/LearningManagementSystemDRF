from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course
from subscription.models import Subscription
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='user@example.com',
            password='password'
        )

        self.course = Course.objects.create(
            title='test course',
            description='test course description'
        )

        self.subscription = Subscription.objects.create(
            is_active=True,
            course=self.course,
            user=self.user
        )

    def test_create_subscription(self):
        self.client.force_authenticate(user=self.user)

        data = {
            'is_active': True,
            'course': self.course.pk
        }

        response = self.client.post(
            reverse('subscription:subscriptions-list'),
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            2
        )

    def test_delete_subscription(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse('subscription:subscriptions-detail', args=[self.subscription.pk]))

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Subscription.objects.all().count(),
            0
        )
