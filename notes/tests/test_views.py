from django.contrib.auth import get_user_model, get_user
from rest_framework.test import APITestCase
from ..views import NoteModelViewSet
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

    def setUp(self):
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
    
    def check_data(self, request, url, title, body, author, id):
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
    
    def check_post_request(self, url, title, body):
        request = self.client.post(url, {
            'title': title,
            'body': body
        }, format='json')
        self.assertEqual(request.status_code, 201)
    
    def check_get_request(self, url):
        request = self.client.get(url)
        self.assertEqual(request.status_code, 200)
        return request

    def loging_user_test(self, username, password):
        logged_in = self.client.login(
            username=username,
            password=password
            )
        self.assertTrue(logged_in)
        current_user = get_user(self.client)
        self.assertEqual(current_user.username, username)
    
    def test_create_note(self):
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
            'http://testserver/api/v1/auth/users/1/',
            id=0
        )

        # Create new user for check links with notes
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
            'http://testserver/api/v1/auth/users/2/',
            id=1
        )