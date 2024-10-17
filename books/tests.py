from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.book_data = {'title': 'Test Book'}
        self.book = Book.objects.create(**self.book_data)

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        new_book = {'title': 'Another Book'}
        response = self.client.post('/api/books/', new_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book(self):
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        updated_data = {'title': 'Updated Title'}
        response = self.client.put(f'/api/books/{self.book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
