from  django.test import  TestCase
from  .models import  Menu 

class MenuTest(TestCase):
     
    def test_get_item(self):
        item = Menu.objects.create(Title="noodle", Price=20 Inventory=20)
        self.assertEqual(str(item), 'noodle:20')
