
from rest_framework.response import Response

from services.models import SystemInfoModel, RestoranModel, BookedDate, EvantModel, ServiceModel, MenuItemModel, MenuModel, Order

from services.serializers.system_serializer import SystemSerializer
from services.serializers.restoran_serializer import RestoranSerializer, EvantSerializer
from services.serializers.service_serializer import ServiceSerializer
from services.serializers.restoran_serializer import MenuItemSerializer, MenuSerializer
from services.serializers.order_serializer import OrderGetSerializer, OrderPostSerializer

from rest_framework import permissions, generics

from rest_framework.decorators import action
from rest_framework.response import Response


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class SystemView(generics.ListAPIView):
    serializer_class = SystemSerializer 
    queryset = SystemInfoModel.objects.all()
    permission_classes = [IsAdminUser]
    
class MenuItemsView(generics.ListAPIView):
    serializer_class = MenuItemSerializer
    queryset = MenuItemModel.objects.all()
    permission_classes = [IsAdminUser]

class MenuView(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = MenuModel.objects.all()
    permission_classes = [IsAdminUser]
    

class RestoranView(generics.ListAPIView):
    serializer_class = RestoranSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
            city = self.request.user.city
            date = self.request.user.event_date
            events_id = self.request.query_params.get("id")
            print(events_id)
            restorans = RestoranModel.objects.filter(event_id=events_id).all()
            booked_dates = BookedDate.objects.filter(date=date).values_list('booked_dates_id', flat=True)
            if booked_dates.exists():
                restorans = restorans.exclude(id__in=booked_dates)
                # restorans.filter(event_id=1)
                return RestoranModel.objects.filter(id__in=restorans, city=city)
            return restorans.filter(city=city)

class EvantView(generics.ListAPIView):
    serializer_class = EvantSerializer 
    queryset = EvantModel.objects.all()
    permission_classes = [IsAdminUser]

class ServiceView(generics.ListAPIView):
    serializer_class = ServiceSerializer 
    queryset = ServiceModel.objects.all()
    permission_classes = [IsAdminUser]


class OrderView(generics.ListAPIView):
    serializer_class = OrderGetSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = OrderPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user

        total_price = 0
        menu = MenuModel.objects.get(pk=request.data.get("menu"))
        gests_amount = request.data.get("gests_amount")
        services = ServiceModel.objects.filter(pk__in=request.data.get('service')).all()
        for service in services:
            total_price += service.price
        total_price += menu.price * gests_amount
        serializer.validated_data['day'] = self.request.user.event_date

        serializer.save(total_price=total_price, )

        restoran_id = request.data.get('restoran')
        restoran = RestoranModel.objects.get(id=restoran_id)
        date_user = self.request.user.event_date 
        booked_dates = BookedDate.objects.create(date=date_user, booked_dates=restoran)
        unique_together = ('date', 'booked_dates')

        return Response(data=serializer.data)