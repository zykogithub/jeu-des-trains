from django.test import TestCase

class FirtTest(TestCase) :
    def setUp(self):
        return super().setUp()
    def test_first(self) :
        self.assertEqual(1,1)