from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} - {self.title}'


    @property
    def owner(self):
        return self.user