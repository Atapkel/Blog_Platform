from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Post, Comment


class CommentEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user1 = User.objects.create_user(username='user1', password='test123')
        self.user2 = User.objects.create_user(username='user2', password='test123')

        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post',
            author=self.user1,
            category='Technology'
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user1,
            content='This is a test comment'
        )

        self.comment_url = reverse('comment-list-create')
        self.post_comments_url = reverse('post-comments', kwargs={'post_id': self.post.id})

    def test_get_comments_allows_unauthenticated_access(self):
        response = self.client.get(self.comment_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('This is a test comment', str(response.data))

    def test_post_comment_requires_authentication(self):
        response = self.client.post(self.comment_url, {
            'post': self.post.id,
            'content': 'New comment without login'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_post_comment(self):
        self.client.login(username='user2', password='test123')
        response = self.client.post(reverse('comment-list-create'), {
            'post': self.post.id,
            'author': self.user2.id,
            'content': 'New comment from logged in user'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.filter(post=self.post).count(), 2)


