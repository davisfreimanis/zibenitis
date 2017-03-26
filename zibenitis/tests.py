from django.test import TestCase
from django.core.urlresolvers import reverse


# Create your tests here.
class FlatpageUrlTest(TestCase):
    def test_donate_url(self):
        url = reverse('donate')
        self.assertEqual(url, '/donate/')
