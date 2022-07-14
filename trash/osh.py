from django.db import models


class Osh(models.Model):
    restaurant = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='wedding_hall/', blank=True, null=True)
    file = models.FileField(upload_to='wedding_hall/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Osh, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.restaurant


class OshMenu(models.Model):
    image = models.ImageField(upload_to='menuitems/', blank=True, null=True)
    name = models.CharField(max_length=30)
    menu_id = models.ForeignKey(Osh, related_name='menu', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(OshMenu, self).save(*args, **kwargs)