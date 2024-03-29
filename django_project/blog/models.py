from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)   # If user deleted, posts are not deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Ensures we are redirected after creating a new post to the post's page."""
        return reverse('post-detail', kwargs={'pk': self.pk})
