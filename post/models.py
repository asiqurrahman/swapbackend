from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from user.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    trade = models.CharField(max_length=100)
    trade_description = models.TextField(null=True)
    wanted = models.CharField(max_length=100)
    wanted_description = models.TextField(null=True)
    trade_image = models.ImageField()
    wanted_image = models.ImageField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.trade
