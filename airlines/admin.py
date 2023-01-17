from django.contrib import admin
from .models import Airline, Order
from import_export.admin import ImportExportModelAdmin
from .resource import AirlineResource,OrderResource


# class AirlineAdmin(admin.ModelAdmin):
#     list_display = ('starting_airport', 'destination_airport', 'airlines','flight','departure_time','arrival_time')

class AirlineAdmin(ImportExportModelAdmin):
    resource_class = AirlineResource
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource

admin.site.register(Airline, AirlineAdmin)
admin.site.register(Order, OrderAdmin)
