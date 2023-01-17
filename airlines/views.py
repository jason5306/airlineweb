from django.shortcuts import render, get_object_or_404
from .models import Airline, Order
from .filters import AirlineFilter
from django.views.generic import DetailView, CreateView, UpdateView, View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse

import random
from .forms import ChooseSeatForm, CheckBagForm, AddOrderForm, SubmitOrderForm, SurveyForm


def search(request, pk):
    airlines = Airline.objects.none()
    airlineFilter = AirlineFilter(queryset=airlines)

    if request.method == "POST":
        airlineFilter = AirlineFilter(request.POST, queryset=Airline.objects.all())

    context = {
        'airlineFilter': airlineFilter,
        'order_id': pk
    }

    return render(request, 'airlines/search.html', context)

def AirlineDetailView(request, aid, oid):
    print(aid)
    print(oid)
    airline = get_object_or_404(Airline, id=aid)

    current_order =get_object_or_404(Order, id=oid)
    carbon_offset_choice = current_order.carbon_choice
    print(carbon_offset_choice)

    context = {
        "airline":airline,
        "carbon_offset_choice":int(carbon_offset_choice),
        "current_order":current_order.pk,
        "carbon_offset_fee":50,
        "choice_0":0,
        "choice_1":1,
        "choice_2":2,
        "choice_3":3
        

    }
    return render(request, 'airlines/airline_detail.html', context)

# class AirlineDetailView(DetailView):
#     model = Airline
#     template_name = 'airlines/airline_detail.html'

#     def get_context_data(self, *args, **kwargs):
#         #cat_menu = Category.objects.all()
#         context = super(AirlineDetailView, self).get_context_data(
#             *args, **kwargs)
#         print(self)

        
#         current_order = Order.objects.last()
#         carbon_offset_choice = current_order.carbon_choice
#         print(carbon_offset_choice)


#         # context data
#         context['carbon_offset_choice'] = int(carbon_offset_choice)
#         context['choice_0'] = 0
#         context['choice_1'] = 1
#         context['choice_2'] = 2
#         context['choice_3'] = 3
#         context['carbon_offset_fee'] = 50
#         context['current_order'] = current_order.pk
#         # context['post'] = current_post
#         return context

class AddOrderView(CreateView):
    model = Order
    template_name = 'airlines/new_order.html'
    form_class = AddOrderForm
 

class SubmitOrderView(UpdateView):
    model = Order
    template_name = 'airlines/comfirm_order.html'
    # fields = '__all__'
    form_class = SubmitOrderForm
    pk_url_kwarg = 'oid'
    
    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])

    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        return reverse_lazy("survey", kwargs={'pk': current_order.pk})

    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(SubmitOrderView, self).get_context_data(
            *args, **kwargs)
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = current_order.carbon_choice

        # context data
        context['current_order'] = current_order.pk
        context['carbon_offset_choice'] = int(carbon_offset_choice)
        context['carbon_offset_fee'] = 50
        context['airline_id'] = self.kwargs["aid"]
        # context['post'] = current_post
        return context  

class ChooseSeatView(UpdateView):
    model = Order
    template_name = 'airlines/choose_seat.html'
    form_class = ChooseSeatForm
    pk_url_kwarg = 'oid'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])
    
    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        return reverse_lazy("check_bag", kwargs={'oid': current_order.pk, 'aid':self.kwargs["aid"]})
    
    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(ChooseSeatView, self).get_context_data(
            *args, **kwargs)
        current_order = Order.objects.get(id=self.kwargs["oid"])
        
        # context data
        context['current_order'] = current_order.pk
        context['airline_id'] = self.kwargs["aid"]

        
        # context['post'] = current_post
        return context  
    
class CheckBagView(UpdateView):
    model = Order
    template_name = 'airlines/check_bag.html'
    form_class = CheckBagForm
    pk_url_kwarg = 'oid'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])

    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = int(current_order.carbon_choice)
        return_page = "carbon_offset"
        if carbon_offset_choice == 0 or carbon_offset_choice == 3: # control group &  compulsory fee group
            return_page = "submit_order"
        print(return_page)

        return reverse_lazy(return_page, kwargs={'oid': current_order.pk, 'aid':self.kwargs["aid"]})


    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(CheckBagView, self).get_context_data(
            *args, **kwargs)
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = current_order.carbon_choice
        # context data
        context['carbon_offset_choice'] = int(carbon_offset_choice)
        context['current_order'] = current_order.pk
        context['carbon_offset_fee'] = 50
        context['airline_id'] = self.kwargs["aid"]
        # context['post'] = current_post
        return context     


class CarbonOffsetView(UpdateView):
    model = Order
    template_name = 'airlines/carbon_offset.html'
    fields = ()
    pk_url_kwarg = 'oid'

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs['oid'])


    def get_success_url(self):
        current_order = Order.objects.get(id=self.kwargs["oid"])
        return reverse_lazy("submit_order", kwargs={'oid': current_order.pk, 'aid':self.kwargs["aid"]})

    def get_context_data(self, *args, **kwargs):
        #cat_menu = Category.objects.all()
        context = super(CarbonOffsetView, self).get_context_data(
            *args, **kwargs) 
        current_order = Order.objects.get(id=self.kwargs["oid"])
        carbon_offset_choice = current_order.carbon_choice

        # context data
        context['carbon_offset_choice'] = int(carbon_offset_choice)
        context['choice_0'] = 0
        context['choice_1'] = 1
        context['choice_2'] = 2
        context['choice_3'] = 3
        context['carbon_offset_fee'] = 50
        context['current_order'] = current_order.pk
        context['airline_id'] = self.kwargs["aid"]
        # context['post'] = current_post
        return context                

class SurveyView(UpdateView):
    model = Order
    template_name = 'airlines/survey.html'
    form_class = SurveyForm
    success_url = reverse_lazy('new_order')
