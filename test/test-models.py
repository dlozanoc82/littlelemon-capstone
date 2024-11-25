from django.test import TestCase
from Restaurant.models import MenuItem
from Restaurant.serializers import MenuItemSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title = "IceCream", price=80, inventory = 100)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "IceCream:80")

class MenuViewTest(TestCase):
    def setUp(self):
        """
        Configura las instancias del modelo Menu para las pruebas.
        """
        self.menu1 = MenuItem.objects.create(name="Pizza", price=10.99, description="Delicious cheese pizza")
        self.menu2 = MenuItem.objects.create(name="Pasta", price=8.99, description="Creamy Alfredo pasta")
        self.menu3 = MenuItem.objects.create(name="Salad", price=5.99, description="Fresh garden salad")

    def test_getall(self):
        """
        Prueba para recuperar todos los objetos Menu.
        """
        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        expected_data = serializer.data

        # Simula una solicitud a la vista correspondiente (ajusta la URL según tu configuración)
        response = self.client.get("/api/menu/")  

        # Verifica que la respuesta sea 200 OK
        self.assertEqual(response.status_code, 200)

        # Verifica que los datos serializados coincidan con los datos de respuesta
        self.assertEqual(response.json(), expected_data)