from django.db import models


class Banquet(models.Model):
    restaurant = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='wedding_hall/', blank=True, null=True)
    file = models.FileField(upload_to='systeminfo/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Banquet, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.restaurant

class BanquetMenu(models.Model):
    image = models.ImageField(upload_to='menuitems/', blank=True, null=True)
    name = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    menu_id = models.ForeignKey(Banquet, related_name='menu', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(BanquetMenu, self).save(*args, **kwargs)