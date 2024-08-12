from django.test import TestCase
from restaurant import models, serializers, views
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.menu1 = models.Menu.objects.create(title="Pancake", price=5, inventory=30)
        self.menu2 = models.Menu.objects.create(title="Cream", price=2, inventory=80)

        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        
    def test_all(self):
        url = reverse('restaurant:menu')
        response = self.client.get(url)
        items = models.Menu.objects.all()
        serializer = serializers.MenuSerializer(items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        