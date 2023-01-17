from dataclasses import fields
from django import forms
from .models import Order
import random




class SubmitOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['starting_airport'].required = False 
        # self.fields['destination_airport'].required = False 
        # self.fields['airlines'].required = False 
        # self.fields['flight'].required = False 
        # self.fields['aircraft_type'].required = False 
        # self.fields['departure_time'].required = False 
        # self.fields['arrival_time'].required = False 
        # self.fields['punctuality_rate'].required = False 
        # self.fields['seat_number'].required = False 
        # self.fields['check_bag'].required = False 
        # self.fields['price'].required = False 
        # self.fields['total_price'].required = False 
        # self.fields['carbon_choice'].required = False 
        
        

    class Meta:
        model = Order
        fields = ('starting_airport','destination_airport', 'airlines', 'flight', 'aircraft_type', 'departure_time', 'arrival_time','punctuality_rate', 'seat_number','check_bag', 'price', 'total_price','carbon_choice')
        widgets = {
            
            'starting_airport': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'destination_airport': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'airlines': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'flight': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'aircraft_type': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'departure_time': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'arrival_time': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'punctuality_rate': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'seat_number': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'check_bag': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'total_price': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),
            'carbon_choice': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden', 'value': ''}),

            
        }

class AddOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddOrderForm, self).__init__(*args, **kwargs)
        self.fields['carbon_choice'].initial = random.randint(0,3)

    class Meta:
        model = Order
        fields = ('carbon_choice',)
        widgets = {
            
            'carbon_choice': forms.TextInput(attrs={'class': 'form-control', 'type':'hidden'}),
            
        }



seat_choice_list = (
            ("Due to covid-19 safety policies, there are limited seating options","Due to covid-19 safety policies, there are limited seating options"),
    )

class ChooseSeatForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('seat_number',)
        labels = {
            "seat_number":  "Choose A Seat",
        }
        widgets = {
            
            'seat_number': forms.Select(choices=seat_choice_list, attrs={'class': 'form-control'}),
            
        }

bag_choice_list = (
            ("7kg cabin baggage (+0 CNY)","7kg cabin baggage (+0 CNY)"),
            ("7kg cabin baggage and 23kg checked baggage (+10CNY)","7kg cabin baggage and 23kg checked baggage (+10CNY)"),
            ("7 kg cabin baggage and two 23kg checked baggage (+50CNY)","7 kg cabin baggage and two 23kg checked baggage (+50CNY)"),
    )
class CheckBagForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('check_bag',)
        labels = {
            "check_bag":  "Choose A Check Bag Option",
        }
        widgets = {
            
            'check_bag': forms.Select(choices=bag_choice_list, attrs={'class': 'form-control'}),
            
        }

subject_gender_list = (
    ("Male","Male"),
    ("Female","Female")
)
subject_age_list = (
    ("18-24","18-24"),
    ("25-34","25-34"),
    ("35-44","35-44"),
    ("45-54","45-54"),
    ("55-64","55-64"),
    ("65+","65+")
)
subject_marital_list = (
    ("Single","Single"),
    ("Married","Married"),
    ("Divorced","Divorced"),
    ("Widowed","Widowed")
)
reply_options = (
    ('Disagree completely','Disagree completely'),
    ('Disagree quite a lot','Disagree quite a lot'),
    ('Disagree to some extent','Disagree to some extent'),
    ('I am not sure','I am not sure'),
    ('Agree to some extent', 'Agree to some extent'),
    ('Agree quite a lot','Agree quite a lot'),
    ('Agree completely','Agree completely')
)
Q2_options = (
    ('No','No'),
    ('Yes - just briefly','Yes - just briefly'),
    ('Yes - quite a lot','Yes - quite a lot')
)
Q4_options = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)
Q6_options = (
    ('No','No'),
    ('Yes - and I did not like it','Yes - and I did not like it'),
    ('Yes - and I was ok with it','Yes - and I was ok with it')
)

class SurveyForm(forms.ModelForm):  
    class Meta:
        model = Order
        fields = ('subject_gender','subject_age','subject_marital','survery_Q1_a','survery_Q1_b','survery_Q1_c','survery_Q1_d','survery_Q1_e','survery_Q2','survery_Q3_a','survery_Q3_b','survery_Q3_c','survery_Q3_d','survery_Q4_a','survery_Q4_b','survery_Q4_c','survery_Q4_d','survery_Q4_e','survery_Q5_a','survery_Q5_b','survery_Q5_c','survery_Q5_d','survery_Q5_e','survery_Q5_f','survery_Q5_g','survery_Q6')
        labels = {
            "subject_gender":  "Your gender:",
            "subject_age": "Your age:",
            "subject_marital":"Your marital status:"
        }
        widgets = {
            
            'subject_gender': forms.Select(choices=subject_gender_list, attrs={'class': 'form-control'}),
            'subject_age': forms.Select(choices=subject_age_list, attrs={'class': 'form-control'}),
            'subject_marital': forms.Select(choices=subject_marital_list, attrs={'class': 'form-control'}),
            
            'survery_Q1_a' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q1_b' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q1_c' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q1_d' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q1_e' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            
            'survery_Q2' :forms.Select(choices=Q2_options, attrs={'class': 'form-control'}),
            
            'survery_Q3_a' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q3_b' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q3_c' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            'survery_Q3_d' :forms.Select(choices=reply_options, attrs={'class': 'form-control'}),
            
            'survery_Q4_a': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q4_b': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q4_c': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q4_d': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q4_e': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            
            'survery_Q5_a': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q5_b': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q5_c': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q5_d': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q5_e': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q5_f': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),
            'survery_Q5_g': forms.TextInput(attrs={'class': 'form-control', 'type':'', 'value': '','required':'required'}),

            'survery_Q6' :forms.Select(choices=Q6_options, attrs={'class': 'form-control'}),
            
        }