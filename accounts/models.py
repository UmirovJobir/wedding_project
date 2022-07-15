from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.exceptions import ValidationError

def validate_length(value,length=9):
    if value.isdigit():
        if len(str(value))!=length:
            raise ValidationError(f"Ошибка: Номер должен содержать {length} цифр.")
    else:
        raise ValidationError("Ошибка: Пишите только цифры.")

class UserModel(AbstractUser):

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
    
    username = models.CharField(max_length=30)
    number = models.CharField(max_length=9, unique=True, validators=[validate_length])
    city = models.CharField(max_length=50, choices=CITY)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Пользователи"
    


 