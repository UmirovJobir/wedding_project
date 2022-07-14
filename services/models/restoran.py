from django.db import models
from accounts.models import UserModel


class EvantModel(models.Model):
    image = models.ImageField(upload_to='files/', blank=True)
    name = models.CharField(max_length=30)
    active = models.BooleanField()

    def save(self, *args, **kwargs):
        super(EvantModel, self).save(*args, **kwargs)
 
    def __str__(self):
        return self.name

class RestoranModel(models.Model):
    restoran = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restoran/', blank=True, null=True)
    file = models.FileField(upload_to='restoran/', blank=True, null=True)
    event_id = models.ManyToManyField(EvantModel, related_name='restorans')

    def save(self, *args, **kwargs):
        super(RestoranModel, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.restoran


class MenuModel(models.Model):
    type = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    restoran_id = models.ForeignKey(RestoranModel, related_name='menus', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(MenuModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


class MenuItemModel(models.Model):
    image = models.ImageField(upload_to='menuitems/', blank=True, null=True)
    itam_name = models.CharField(max_length=30)
    menu_id = models.ForeignKey(MenuModel, related_name="menuitems", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(MenuItemModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.itam_name

class BookedDate(models.Model):
    date = models.DateField()
    booked_dates = models.ForeignKey(RestoranModel, related_name="booked_dates", on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.booked_dates}: {self.date}')

    class Meta: 
        unique_together = ('date', 'booked_dates')