from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.db import models
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


class LoginRequiredMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@example.com', 'foo')

    def test_anonymous(self):
        url = reverse('login_required')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_authenticated(self):
        self.client.login(username='test', password='foo')
        response = self.client.get(reverse('login_required'))
        self.assertEqual(response.status_code, 200)


class PermissionRequiredMixinTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@example.com', 'foo')

    def test_missing_permission(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('missing_permission'))

    def test_bad_permission(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('bad_permission'))

    def test_user_lacks_permission(self):
        self.client.login(username='test', password='foo')
        url = reverse('add_user_permission')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_raise_403(self):
        self.client.login(username='test', password='foo')
        response = self.client.get(reverse('add_user_permission_403'))
        self.assertEqual(response.status_code, 403)

    def test_user_has_permission(self):
        permission = Permission.objects.get(codename='add_user')
        self.user.user_permissions.add(permission)
        self.client.login(username='test', password='foo')
        response = self.client.get(reverse('add_user_permission'))
        self.assertEqual(response.status_code, 200)
