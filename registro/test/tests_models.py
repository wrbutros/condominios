from django.test import TestCase
from ..models import Ciudad


class CiudadTestCase(TestCase):

    def create_ciudad(self, nombre="Santiago"):
        return Ciudad.objects.create(nombre=nombre)

    def test_ciudad_creation(self):
        c = self.create_ciudad()
        self.assertTrue(isinstance(c, Ciudad))
        self.assertEqual(c.__unicode__(), c.nombre)
