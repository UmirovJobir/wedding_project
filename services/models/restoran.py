from difflib import restore
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

    class Meta:
         verbose_name_plural = "Мероприятие"

class RestoranModel(models.Model):

    TOSHKENT = "Toshkent"
    TOSHKENT_V = "Toshkent_v"
    ANDIJON = "Andijon "
    BUXORO = "Buxoro"
    FARGONA = "Farg'ona"
    SIRDARYO = "Sirdaryo"
    JIZZAX = "Jizzax"
    NAMANGAN = "Namangan"
    NAVOIY = "Navoiy"
    QORAQAL = "Qoraqalpog'iston Respublikasi"
    SAMARQAND = "Samarqand"
    SURXONDARYO = "Surxondaryo"
    XORAZM = "Xorazm"
    QASHQADARYO = "Qashqadaryo"

    CITY = (
        (TOSHKENT, "Toshkent"),
        (TOSHKENT_V, "Toshkent_v"),
        (ANDIJON, "Andijon"),
        (BUXORO, "Buxoro"),
        (FARGONA, "Farg'ona"),
        (SIRDARYO, "Sirdaryo"),
        (JIZZAX, "Jizzax"),
        (NAMANGAN, "Namangan"),
        (NAVOIY, "Navoiy"),
        (QORAQAL, "Qoraqalpog'iston Respublikasi"),
        (SAMARQAND, "Samarqand"),
        (SURXONDARYO, "Surxondaryo"),
        (XORAZM, "Xorazm"),
        (QASHQADARYO, "Qashqadaryo"),
    )

    restoran = models.CharField(max_length=30)
    city = models.CharField(max_length=30, choices=CITY)
    address = models.CharField(max_length=50)
    image = models.ImageField(upload_to='restoran/', blank=True, null=True)
    file = models.FileField(upload_to='restoran/', blank=True, null=True)
    event_id = models.ManyToManyField(EvantModel, related_name='restorans_id')

    def save(self, *args, **kwargs):
        super(RestoranModel, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.restoran

    class Meta:
         verbose_name_plural = "Ресторан"


class TableModel(models.Model):
    table_name = models.CharField(max_length=50)
    type_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    restoran_id = models.ForeignKey(RestoranModel, related_name='tables', on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class BookedDate(models.Model):
    date = models.DateField()
    restoran_id = models.ForeignKey(RestoranModel, related_name='restoran_id', on_delete=models.CASCADE)

    def __str__(self):
        return str(f'{self.restoran_id}: {self.date}')

    class Meta: 
        unique_together = ('date', 'restoran_id')
        verbose_name_plural = "Забронированные даты"
    