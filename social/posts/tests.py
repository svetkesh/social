from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='user123', password='password123')
        testuser1.save()
        test_post = Post.objects.create(
            author=testuser1, body='Body about...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)

        author = f'{post.author}'
        body = f'{post.body}'
        self.assertEqual(author, 'user123')
        self.assertEqual(body, 'Body about...')
