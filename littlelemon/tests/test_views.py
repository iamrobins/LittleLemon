from django.test import TestCase
from restaurant.models import Menu


class MenuViewSet(TestCase):
    def setUp(self):
        Menu.objects.create(name = 'Salad', price = 12.00, stock = 8)
        Menu.objects.create(name = 'Pasta', price = 9.00, stock = 12)
        
    def test_getall(self):
        instance1 = Menu.objects.get(name = 'Salad')
        instance2 = Menu.objects.get(name = 'Pasta')
        self.assertEqual(instance1.__str__(), "Salad : 12.00")
        self.assertEqual(instance2.__str__(), "Pasta : 9.00")