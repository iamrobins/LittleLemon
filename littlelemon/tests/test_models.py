from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name = "Pizza", price = 7.00, stock = 12)
        self.assertEqual(item.__str__(), "Pizza : 7.0")