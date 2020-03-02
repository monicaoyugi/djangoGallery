from django.test import TestCase
from .models import  Location, Category, Image


class LocationTestClass(TestCase):

    def setUp(self):
        self.new_location(location_name = Location)


    def tearDown(self):
        Location.objects.all().delete()

    def test_save_location_method(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location))

    def test_update_location_metho(self):
        self.new_location.save_location()
        updated_location = Location.updated_location(self.new_location.id,'Kenya')
        self.assertEqual(updated_location.location, 'Kenya')


    def test_delete_location_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

