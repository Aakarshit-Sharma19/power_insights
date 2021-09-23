from django.db import models
from accounts.models import User
from django.utils import timezone
# Create your models here.


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    consumption = models.DecimalField(
        default=0, max_digits=7, decimal_places=3)
