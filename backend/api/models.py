from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes")
    #  on_delete=models.CASCADE means if the user is deleted then the the related notes will also be deleted
    # related_name="notes" by this i can access notes in User

    def __str__(self):
        return self.title
