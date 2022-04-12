from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    phone = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username
