from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagersTests(TestCase):
    def test_case_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='example',
            email='example@user.com',
            password='foo',
            gender='Catgirl'
        )
        self.assertEqual(user.username, 'example')
        self.assertEqual(user.email, 'example@user.com')
        self.assertEqual(user.gender, 'Catgirl')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='', email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', email='', password='foo')
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='sudo_example',
            email='super@user.com',
            password='foo',
        )
        self.assertEqual(admin_user.username, 'sudo_example')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertEqual(admin_user.gender, 'i will not say')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='example',
                email='super@user.com',
                password='foo',
                is_superuser=False
            )