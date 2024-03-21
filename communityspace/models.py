from django.db import models
from User.models import User
# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{User.user.email}"
