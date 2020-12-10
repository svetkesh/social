from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ' '.join(self.body.split()[:5]).capitalize() + '...'


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.author) + ' likes post ' + str(self.post.id)


class Dislike(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        related_name='dislikes',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.author) + ' hates post ' + str(self.post.id)
