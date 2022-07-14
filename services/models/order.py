from django.db import models
from accounts.models import UserModel
from services.models import RestoranModel, MenuModel, ServiceModel, ServiceModel



class Order(models.Model):
    IN_PROCESS = "In process"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    STATUS = (
        (IN_PROCESS, "In process"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled")
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.DateField(blank=True)
    restoran = models.ForeignKey(RestoranModel, on_delete=models.CASCADE)
    gests_amount = models.PositiveIntegerField(default=1)
    menu = models.ForeignKey(MenuModel, on_delete=models.CASCADE)
    service = models.ManyToManyField(ServiceModel, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, blank=True, default=IN_PROCESS)
    total_price = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
         verbose_name_plural = "Заказ"

    @property
    def menu_price(self):
        menu_price = self.menu.price
        return menu_price


    @property
    def gests_price_all(self):
        number = int(self.menu_price) * int(self.gests_amount)
        return number
        

    @property
    def service_price(self):
        total_price = 0
        for service in self.service.all():
            total_price += service.price  
        return total_price


