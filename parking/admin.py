from django.contrib import admin
from .models import User, LotType, ParkingLot, ParkingTicket
# Register your models here.


admin.site.register(User)
admin.site.register(LotType)
admin.site.register(ParkingLot)
admin.site.register(ParkingTicket)