# Create your tests here.

from rest_framework.test import APITestCase

from blog.models import Blog, Comments, User
from datetime import datetime

class BlogTest(APITestCase):

    def setUp(self):
        print('setUp')
        Blog.objects.create(id=1,title='test', content='content', summary='summary')

    def test_create_blog(self):
        print('test_create_blog')
        url = '/api/blog/'
        data = {
            "title": "create",
            "content": "create content",
            "summary": " create summary"
        }
        response = self.client.post(url, data, format='json')
        res = response.json()
        status = res.get('status')
        self.assertEqual(status, 2000)
        self.assertEqual(Blog.objects.filter(title="create")[0].content, "create content")
    
    def test_list_blog(self):
        print('test_list_blog')
        url = '/api/blog/'
        response = self.client.get(url)
        res = response.json()
        status = res.get('status')
        summary = res.get('result')[0].get('summary')
        self.assertEqual(status, 2000)
        self.assertEqual(summary, "summary")
    
    def test_count_blog(self):
        print('test_count_blog')
        url = '/api/blog/count/'
        response = self.client.get(url)
        res = response.json()
        status = res.get('status')
        count = res.get('result').get('count')
        self.assertEqual(status, 2000)
        self.assertEqual(count, 1)

    def test_retrieve_blog(self):
        print('test_retrieve_blog')
        url = '/api/blog/1/'
        response = self.client.get(url)
        res = response.json()
        status = res.get('status')
        summary = res.get('result').get('summary')
        self.assertEqual(status, 2000)
        self.assertEqual(summary, 'summary')
    
    def test_update_blog(self):
        print('test_update_blog')
        url = '/api/blog/1/'
        data = {
            "title": "update",
            "content": "update content",
            "summary": " update summary",
        }
        response = self.client.put(url, data, format='json')
        res = response.json()
        status = res.get('status')
        summary = res.get('result').get('summary')
        self.assertEqual(status, 2000)
        self.assertEqual(summary, 'update summary')

    def test_delete_blog(self):
        print('test_delete_blog')
        url = '/api/blog/1/'
        response = self.client.delete(url)
        res = response.json()
        status = res.get('status')
        result = res.get('result')
        self.assertEqual(status, 2000)
        self.assertEqual(result, {})


class CommentTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        print('setUpTestData')
        Blog.objects.create(id=1,title='test', content='content', summary='summary')

    def setUp(self):
        print('setUp')
        Comments.objects.create(id=1,username='test', content='content', blog_id=1)

    def test_create_comment(self):
        print('test_create_comment')
        url = '/api/blog/1/comment/'
        data = {
            "username": "test-create",
            "content": "create comment content"
        }
        response = self.client.post(url, data, format='json')
        res = response.json()
        status = res.get('status')
        self.assertEqual(status, 2000)
        self.assertEqual(Comments.objects.filter(username="test-create")[0].content, "create comment content")

    def test_list_comment(self):
        print('test_list_comment')
        url = '/api/blog/1/comment/'
        response = self.client.get(url)
        res = response.json()
        status = res.get('status')
        username = res.get('result')[0].get('username')
        self.assertEqual(status, 2000)
        self.assertEqual(username, 'test')

    def test_count_comment(self):
        print('test_count_comment')
        url = '/api/blog/1/comment/count/'
        response = self.client.get(url)
        res = response.json()
        status = res.get('status')
        count = res.get('result').get('count')
        self.assertEqual(status, 2000)
        self.assertEqual(count, 1)

    def test_retrieve_comment(self):
        print('test_retrieve_comment')
        url = '/api/blog/1/comment/1/'
        response = self.client.get(url)
        res = response.json()
        status = res.get('status')
        username = res.get('result').get('username')
        self.assertEqual(status, 2000)
        self.assertEqual(username, 'test')
    
    def test_update_comment(self):
        print('test_update_comment')
        url = '/api/blog/1/comment/1/'
        data = {
            "username": "test-create",
            "content": "update comment content"
        }
        response = self.client.put(url, data, format='json')
        res = response.json()
        status = res.get('status')
        content = res.get('result').get('content')
        self.assertEqual(status, 2000)
        self.assertEqual(content, 'update comment content')

    def test_delete_comment(self):
        print('test_delete_comment')
        url = '/api/blog/1/comment/1/'
        response = self.client.delete(url)
        res = response.json()
        status = res.get('status')
        result = res.get('result')
        self.assertEqual(status, 2000)
        self.assertEqual(result, {})



 