from django.db import models
from django.utils import timezone

from accounts.models import User


# Create your models here.


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    consumption = models.DecimalField(
        default=0, max_digits=7, decimal_places=3)
