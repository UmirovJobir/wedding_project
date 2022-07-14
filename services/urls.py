from django.urls import path, include
from rest_framework.routers import DefaultRouter
from services.views import SystemViewset, EvantViewset, ServiceViewset, MenuViewset, MenuItemsViewset, RestoranView, OrderView


router = DefaultRouter()
router.register('system', SystemViewset),
router.register('menuitems', MenuItemsViewset),
router.register('menus', MenuViewset),
router.register('events', EvantViewset)
router.register('services', ServiceViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('restorans/', RestoranView.as_view()),
    path('order/', OrderView.as_view())
]