try:
    import json
except ImportError:
    from django.utils import simplejson as json

from django.conf import settings
from django.contrib.auth.models import User, Permission
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.db import models
from django.test import TestCase
from django.test.client import Client

from .forms import ExampleForm


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@example.com', 'foo')

    def log_user_in(self):
        self.client.login(username='test', password='foo')


class SetHeadlineMixinTestCase(BaseTestCase):
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


class LoginRequiredMixinTestCase(BaseTestCase):
    def test_anonymous(self):
        url = reverse('login_required')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_authenticated(self):
        self.log_user_in()
        response = self.client.get(reverse('login_required'))
        self.assertEqual(response.status_code, 200)


class PermissionRequiredMixinTestCase(BaseTestCase):
    def test_missing_permission(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('missing_permission'))

    def test_bad_permission(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('bad_permission'))

    def test_user_lacks_permission(self):
        self.log_user_in()
        url = reverse('add_user_permission')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_raise_403(self):
        self.log_user_in()
        response = self.client.get(reverse('add_user_permission_403'))
        self.assertEqual(response.status_code, 403)

    def test_user_has_permission(self):
        permission = Permission.objects.get(codename='add_user')
        self.user.user_permissions.add(permission)
        self.log_user_in()
        response = self.client.get(reverse('add_user_permission'))
        self.assertEqual(response.status_code, 200)


class MultiplePermissionsRequiredMixinTestCase(BaseTestCase):
    def test_missing_permissions(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('missing_multiple_permissions'))

    def test_not_a_dict(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('not_a_dict_multiple_permissions'))

    def test_wrong_keys(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('wrong_keys_multiple_permissions'))

    def test_not_a_list(self):
        with self.assertRaises(ImproperlyConfigured):
            self.client.get(reverse('not_a_list_multiple_permissions'))

    def test_all_with_no_permissions(self):
        self.log_user_in()
        url = reverse('all_multiple_permissions')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_all_with_some_permissions(self):
        permission = Permission.objects.get(codename='add_user')
        self.user.user_permissions.add(permission)
        self.log_user_in()
        url = reverse('all_multiple_permissions')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_all_with_all_permissions(self):
        permissions = list(Permission.objects.filter(codename__in=('add_user', 'change_user')))
        self.user.user_permissions.add(*permissions)
        print self.user.user_permissions.all()
        self.log_user_in()
        response = self.client.get(reverse('all_multiple_permissions'))
        self.assertEqual(response.status_code, 200)

    def test_all_raise_403(self):
        self.log_user_in()
        response = self.client.get(reverse('all_multiple_permissions_403'))
        self.assertEqual(response.status_code, 403)

    def test_any_with_no_permissions(self):
        self.log_user_in()
        url = reverse('any_multiple_permissions')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_any_with_some_permissions(self):
        permission = Permission.objects.get(codename='add_user')
        self.user.user_permissions.add(permission)
        self.log_user_in()
        response = self.client.get(reverse('any_multiple_permissions'))
        self.assertEqual(response.status_code, 200)

    def test_any_raise_403(self):
        self.log_user_in()
        response = self.client.get(reverse('any_multiple_permissions_403'))
        self.assertEqual(response.status_code, 403)


class SuperuserRequiredMixinTestCase(BaseTestCase):
    def test_not_superuser(self):
        self.log_user_in()
        url = reverse('superuser_required')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_raise_403(self):
        self.log_user_in()
        response = self.client.get(reverse('superuser_required_403'))
        self.assertEqual(response.status_code, 403)

    def test_superuser(self):
        self.user.is_superuser = True
        self.user.save()
        self.log_user_in()
        response = self.client.get(reverse('superuser_required'))
        self.assertEqual(response.status_code, 200)


class StaffuserRequiredMixinTestCase(BaseTestCase):
    def test_not_staffuser(self):
        self.log_user_in()
        url = reverse('staffuser_required')
        response = self.client.get(url)
        expected_url = '%s?next=%s' % (settings.LOGIN_URL, url)
        self.assertRedirects(response, expected_url)

    def test_raise_403(self):
        self.log_user_in()
        response = self.client.get(reverse('staffuser_required_403'))
        self.assertEqual(response.status_code, 403)

    def test_staffuser(self):
        self.user.is_staff = True
        self.user.save()
        self.log_user_in()
        response = self.client.get(reverse('staffuser_required'))
        self.assertEqual(response.status_code, 200)


class UserKwargModelFormMixinTestCase(BaseTestCase):
    def test_user_form(self):
        form = ExampleForm(user=self.user)
        self.assertEqual(form.user, self.user)


class UserFormKwargsMixinTestCase(BaseTestCase):
    def test_user_form(self):
        self.log_user_in()
        response = self.client.get(reverse('user_form_kwargs'))
        form = response.context['form']
        self.assertEqual(form.user, self.user)


class CsrfExemptMixinTestCase(BaseTestCase):
    def setUp(self):
        super(CsrfExemptMixinTestCase, self).setUp()
        self.csrf_client = Client(enforce_csrf_checks=True)
        self.csrf_client.cookies[settings.CSRF_COOKIE_NAME] = 'csrf'

    def test_correct_csrf_token(self):
        response = self.csrf_client.post(reverse('csrf_exempt'), {
            'csrfmiddlewaretoken': 'csrf',
        })
        self.assertEqual(response.status_code, 200)

    def test_missing_csrf_token(self):
        response = self.csrf_client.post(reverse('csrf_exempt'))
        self.assertEqual(response.status_code, 200)


class JSONResponseMixinTestCase(BaseTestCase):
    def test_content_type(self):
        response = self.client.get(reverse('json_response'))
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_response_contents(self):
        response = self.client.get(reverse('json_response'))
        data = json.loads(response.content)
        self.assertEqual(data['status'], 'ok')
