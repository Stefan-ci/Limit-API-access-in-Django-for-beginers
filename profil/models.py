from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=200, unique=True, editable=False)
    hashed_api_key = models.CharField(max_length=200, unique=True, editable=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']



    def __str__(self):
        try:
            return str(self.user.email)
        except:
            return str(self.user.username)