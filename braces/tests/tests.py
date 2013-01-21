from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.test import TestCase


class SetHeadlineMixinTestCase(TestCase):
    def test_missing_headline(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('missing_headline'))

    def test_static_headline(self):
        response = self.client.get(reverse('static_headline'))
        self.assertIn('headline', response.context)
        self.assertEqual(response.context['headline'], "Quick brown fox")

    def test_dynamic_headline(self):
        response = self.client.get(reverse('dynamic_headline'))
        self.assertIn('headline', response.context)
        self.assertEqual(response.context['headline'], "Quick brown fox")

