
from django.contrib import admin
from django.contrib.auth.models import Group

from services.models.system_info import SystemInfoModel, SystemInfoFileModel
from services.models.service import ServiceModel, Category
from services.models.restoran import MenuItemModel, MenuModel, RestoranModel, BookedDate, EvantModel
from services.models.order import Order
from rest_framework.authtoken.models import TokenProxy


import nested_admin

admin.site.unregister(TokenProxy)
admin.site.unregister(Group)

class SystemInfoFileInline(nested_admin.NestedStackedInline):
    model = SystemInfoFileModel
class SystemInfoAdmin(nested_admin.NestedModelAdmin):
    inlines = [SystemInfoFileInline,]
admin.site.register(SystemInfoModel, SystemInfoAdmin)

admin.site.register(EvantModel)
# admin.site.register(RestoranModel)
# admin.site.register(MenuModel)
# admin.site.register(MenuItemModel)

class MenuItemsInline(nested_admin.NestedStackedInline):
    model = MenuItemModel  
class MenuAdminInline(nested_admin.NestedStackedInline):
    model = MenuModel
    inlines = [MenuItemsInline]
class RestoranAdmin(nested_admin.NestedModelAdmin):
    inlines = [MenuAdminInline]
admin.site.register(RestoranModel, RestoranAdmin)
admin.site.register(BookedDate)



class ServicesInline(nested_admin.NestedStackedInline):
    model = ServiceModel
class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [ServicesInline,]
admin.site.register(Category, CategoryAdmin)

admin.site.register(Order)
