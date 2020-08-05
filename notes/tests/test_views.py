from __future__ import annotations
from django.contrib.auth import get_user_model, get_user
from rest_framework.test import APITestCase
from ..views import NoteModelViewSet
from rest_framework.response import Response
import json


class NotesTests(APITestCase):
    '''
    Django rest test case for testing basic logic of Notes
    Notes fields:  
    url: "http://testserver/api/v1/notes/1/"
    title: "new ideas"
    body: "lorem ipsum"
    author: "http://testserver/api/v1/auth/users/1/"
    '''

    def setUp(self) -> None:
        User = get_user_model()
        self.user, created_user = User.objects.get_or_create(
            username='testusername',
            email='example@user.com'
        )
        self.user.set_password('testuserpass')
        self.user.save()
        self.second_user = User.objects.create_superuser(
            username='sudo_user',
            email='super@user.com',
            password='testsudopass'
        )
        self.second_user.set_password('testsudopass')
        self.second_user.save()
        self.view = NoteModelViewSet.as_view(actions={'get': 'retrieve'})
    
    def check_data(self, request: Response, url, title, body, author, id) -> None:
        response_data = json.loads(request.content)
        self.assertEqual(
            response_data[id]['url'],
            url
        )
        self.assertEqual(
            response_data[id]['title'],
            title
        )
        self.assertEqual(
            response_data[id]['body'],
            body
        )
        self.assertEqual(
            response_data[id]['author'],
            author
        )
    
    def check_post_request(self, url: str, title: str, body: str) -> None:
        request = self.client.post(url, {
            'title': title,
            'body': body
        }, format='json')
        self.assertEqual(request.status_code, 201)

    def check_put_patch_request(self, url: str, method: str, **kwargs) -> None:
        if method == 'put':
            request = self.client.put(url, kwargs)
        elif method == 'patch':
            request = self.client.patch(url, kwargs)
        else:
            raise ValueError('method must be put or patch')
        self.assertEqual(request.status_code, 200)
    
    def check_delete_request(self, url: str) -> None:
        request = self.client.delete(url)
        self.assertEqual(request.status_code, 204)
    
    def check_get_request(self, url: str) -> Response:
        request = self.client.get(url)
        self.assertEqual(request.status_code, 200)
        return request

    def loging_user_test(self, username: str, password: str) -> None:
        logged_in = self.client.login(
            username=username,
            password=password
            )
        self.assertTrue(logged_in)
        current_user = get_user(self.client)
        self.assertEqual(current_user.username, username)
    
    def test_create_note(self) -> None:
        # Create base user and create note for testing association
        self.loging_user_test('testusername', 'testuserpass')
        self.check_post_request(
            '/api/v1/notes/',
            'new ideas',
            'lorem ipsum'
        )
        
        request = self.check_get_request('/api/v1/notes/')

        self.check_data(
            request,
            'http://testserver/api/v1/notes/1/',
            'new ideas',
            'lorem ipsum',
            'http://testserver/api/v1/auth/users/testusername/',
            id=0
        )

        # Create notes as admin user
        self.client.logout()
        self.loging_user_test('sudo_user', 'testsudopass')

        self.check_post_request(
            '/api/v1/notes/',
            'Admin title',
            'Admin body'
        )

        request = self.check_get_request('/api/v1/notes/')

        self.check_data(
            request,
            'http://testserver/api/v1/notes/2/',
            'Admin title',
            'Admin body',
            'http://testserver/api/v1/auth/users/sudo_user/',
            id=1
        )

        # Create notes without account
        self.client.logout()
        with self.assertRaises(ValueError):
            self.check_post_request(
                '/api/v1/notes/',
                'Notes without user',
                'This request must get error code'
            )
    
    def test_put_patch_note(self):
        full_note_path = 'http://testserver/api/v1/notes/1/'
        self.loging_user_test('testusername', 'testuserpass')
        self.check_post_request(
            '/api/v1/notes/',
            'testusername note 2',
            'This is body note 2 bruh'
        )
        self.check_put_patch_request(
            '/api/v1/notes/1/',
            method='put',
            title='i am changed',
            body='That\'s should works...'
        )
        request = self.check_get_request('/api/v1/notes/')
        self.check_data(
            request,
            full_note_path,
            'i am changed',
            'That\'s should works...',
            'http://testserver/api/v1/auth/users/testusername/',
            id=0
        )
        self.check_put_patch_request(
            '/api/v1/notes/1/',
            method='patch',
            body='It\'s another change!'
        )
        request = self.check_get_request('/api/v1/notes/')
        self.check_data(
            request,
            full_note_path,
            'i am changed',
            'It\'s another change!',
            'http://testserver/api/v1/auth/users/testusername/',
            id=0
        )
    def test_delete_note(self):
        self.loging_user_test('testusername', 'testuserpass')
        self.check_post_request(
            '/api/v1/notes/',
            'Create simple note',
            'Body of the simple note'
        )
        self.check_delete_request('/api/v1/notes/1/')
        request = self.client.get('/api/v1/notes/1/')
        self.assertEqual(request.status_code, 404)