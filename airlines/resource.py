from import_export import resources
from .models import Airline, Order

class AirlineResource(resources.ModelResource):

    class Meta:
        model = Airline
        import_id_fields = ['airline_id']

class OrderResource(resources.ModelResource):

    class Meta:
        model = Order
        # import_id_fields = ['order_']