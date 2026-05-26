from django.test import RequestFactory, TestCase


class FirtTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        # request = self.factory.get("/customer/details")
        pass
