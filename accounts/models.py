from django.db import models
from django.contrib.auth.models import  AbstractUser


class UserModel(AbstractUser):
    number = models.CharField(max_length=9, unique=True)
    city = models.CharField(max_length=20)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-date_joined']
    
    def save(self, *args, **kwargs):
        super(UserModel, self).save(*args, **kwargs)


 