from email.policy import default
from django.db import models
from django.urls import reverse

class Order(models.Model):
    starting_airport = models.CharField(max_length=100, default='-')
    destination_airport = models.CharField(max_length=100, default='-')
    #airlines = models.CharField(max_length=100, choices=AIRLINE_CHOICES)
    airlines = models.CharField(max_length=100, default='-')
    flight = models.CharField(max_length=100, default='-')
    aircraft_type = models.CharField(max_length=100, default='-')
    departure_time = models.CharField(blank=True, null=True,max_length=10)
    arrival_time = models.CharField(blank=True, null=True,max_length=10)
    punctuality_rate = models.CharField(max_length=100,default='-')
    seat_number = models.CharField(max_length=100,default='-')
    check_bag = models.CharField(max_length=100,default='-')
    price = models.CharField(max_length=10,default='-')
    total_price = models.CharField(max_length=10,default='-')
    carbon_choice = models.CharField(max_length=10,default='-')
    
    subject_gender = models.CharField(max_length=10,default='-')
    subject_age = models.CharField(max_length=10,default='-')
    subject_marital = models.CharField(max_length=10,default='-')

    survery_Q1_a = models.CharField(max_length=30,default='-')
    survery_Q1_b = models.CharField(max_length=30,default='-')
    survery_Q1_c = models.CharField(max_length=30,default='-')
    survery_Q1_d = models.CharField(max_length=30,default='-')
    survery_Q1_e = models.CharField(max_length=30,default='-')

    survery_Q2 = models.CharField(max_length=30,default='-')
    
    survery_Q3_a = models.CharField(max_length=30,default='-')
    survery_Q3_b = models.CharField(max_length=30,default='-')
    survery_Q3_c = models.CharField(max_length=30,default='-')
    survery_Q3_d = models.CharField(max_length=30,default='-')
    
    survery_Q4_a = models.CharField(max_length=30,blank=True)
    survery_Q4_b = models.CharField(max_length=30,blank=True)
    survery_Q4_c = models.CharField(max_length=30,blank=True)
    survery_Q4_d = models.CharField(max_length=30,blank=True)
    survery_Q4_e = models.CharField(max_length=30,blank=True)

    survery_Q5_a = models.CharField(max_length=30,blank=True)
    survery_Q5_b = models.CharField(max_length=30,blank=True)
    survery_Q5_c = models.CharField(max_length=30,blank=True)
    survery_Q5_d = models.CharField(max_length=30,blank=True)
    survery_Q5_e = models.CharField(max_length=30,blank=True)
    survery_Q5_f = models.CharField(max_length=30,blank=True)
    survery_Q5_g = models.CharField(max_length=30,blank=True)
    
    survery_Q6 = models.CharField(max_length=30,default='-',blank=True)
    
    def get_absolute_url(self):
    # set success url
        return reverse("search", kwargs={'pk': self.pk})


class Airline(models.Model):

    AIRLINE_CHOICES = (
            ("金鹏航空","金鹏航空"),
            ("中国国航","中国国航"),
            ("昆明航空","昆明航空"),
            ("深圳航空","深圳航空"),
            ("海南航空","海南航空"),
            ("南方航空","南方航空"),
            ("厦门航空","厦门航空"),
            ("祥鹏航空","祥鹏航空"),
            ("东方航空","东方航空"),
            ("多彩航空","多彩航空"),
            ("天津航空","天津航空"),
            ("华夏航空","华夏航空"),
            ("山东航空","山东航空"),
            ("长龙航空","长龙航空"),
            ("中国联航","中国联航"),
            ("河北航空","河北航空"),
            ("首都航空","首都航空"),
            ("四川航空","四川航空"),
            ("西藏航空","西藏航空"),
            ("成都航空","成都航空"),
            ("吉祥航空","吉祥航空"),
            ("上海航空","上海航空"),
            ("东海航空","东海航空"),
            ("重庆航空","重庆航空"),
            ("西部航空","西部航空"),
            ("幸福航空","幸福航空"),
            ("福州航空","福州航空"),
            ("瑞丽航空","瑞丽航空"),
            ("桂林航空","桂林航空"),
            ("青岛航空","青岛航空"),
            ("北部湾航空","北部湾航空"),
            ("长安航空","长安航空"),
            ("江西航空","江西航空"),
            ("乌鲁木齐航空","乌鲁木齐航空"),
        
    )
    airline_id = models.IntegerField(default=0)
    starting_airport = models.CharField(max_length=100)
    destination_airport = models.CharField(max_length=100)
    #airlines = models.CharField(max_length=100, choices=AIRLINE_CHOICES)
    airlines = models.CharField(max_length=100)
    flight = models.CharField(max_length=100)
    aircraft_type = models.CharField(max_length=100, default='-')
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    punctuality_rate = models.CharField(max_length=100,default='-')
    price = models.CharField(max_length=10,default='-')

    def get_absolute_url(self):
    #return reverse("article_detail", args=(str(self.pk)))
    #return reverse('home')
        return reverse("arline_detail", kwargs={'pk': self.pk})
    
    
