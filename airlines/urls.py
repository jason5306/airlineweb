from django.urls import path
from .views import search, AirlineDetailView, AddOrderView,SubmitOrderView,ChooseSeatView, CheckBagView, CarbonOffsetView,SurveyView



urlpatterns = [
    path('', AddOrderView.as_view(), name='new_order'),
    path('search/<int:pk>', search, name='search'),
    path('arline_detail/<int:aid>/<int:oid>', AirlineDetailView, name='arline_details'),
    path('submit_order/<int:aid>/<int:oid>', SubmitOrderView.as_view(), name = 'submit_order'),
    path('choose_seat/<int:aid>/<int:oid>', ChooseSeatView.as_view(), name = 'choose_seat'),
    path('check_bag/<int:aid>/<int:oid>', CheckBagView.as_view(), name = 'check_bag'),
    path('carbon_offset/<int:aid>/<int:oid>', CarbonOffsetView.as_view(), name = 'carbon_offset'),
    path('survey/<int:pk>', SurveyView.as_view(), name = 'survey'),
]
