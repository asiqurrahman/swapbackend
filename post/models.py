from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from user.models import User
from django.utils import timezone
from django.utils import timesince

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=CASCADE)
    trade = models.CharField(max_length=100)
    wanted = models.CharField(max_length=100)
    trade_image = models.ImageField()
    trade_image1 = models.ImageField(null=True, blank = True)
    trade_image2 = models.ImageField(null=True, blank = True)
    trade_image3 = models.ImageField(null=True, blank = True)
    trade_image4 = models.ImageField(null=True, blank = True)
    trade_image5 = models.ImageField(null=True, blank = True)
    wanted_image = models.ImageField()
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.trade

    @property
    def timesince(self):
        return timesince.timesince(self.date_posted)






