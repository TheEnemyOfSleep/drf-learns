from django.test import TestCase
from django.contrib.auth import get_user_model, get_user
from ..models import Note


class NoteTestCase(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user, created_user = User.objects.get_or_create(
            username='testuser',
        )
        self.user.set_password('testpass12345')
        self.user.save()

    def test_create_article(self):
        logged_in = self.client.login(
            username='testuser',
            password='testpass12345'
            )
        self.assertTrue(logged_in)
        current_user = get_user(self.client)
        self.assertEqual(current_user.username, 'testuser')
        note = Note(title='Test notes', body='More then test notes')
        note.save()
