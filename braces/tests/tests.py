from django.core.urlresolvers import reverse
from django.test import TestCase


class SetHeadlineMixinTestCase(TestCase):
    def test_static_headline(self):
        response = self.client.get(reverse('static_headline'))
        self.assertIn('headline', response.context)
        self.assertEqual(response.context['headline'], 'Quick brown fox')
