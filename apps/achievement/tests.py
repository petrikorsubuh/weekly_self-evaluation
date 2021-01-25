from django.test import TestCase
from .models import *
# Create your tests here.
from datetime import timedelta,datetime
from apps.achievement.models import Achievement


def date_filter(start_date,end_date):
    poin = []
    while start_date!=end_date and start_date<end_date:
        box = [] #coba cek apakah box nambah terus --> solusi
        obj =Achievement.objects.filter(date=start_date)
        for o in obj:
            if o.target_set==o.actual or o.target_set==o.actual:
                box.append(1)
            else:
                box.append(0)
        sum_box = sum(box)
        if sum_box ==0:
            poin.append(0.0)
        else:
            ppw = sum_box/len(box)*100
            poin.append(round(ppw,2))

        start_date+=timedelta(days=7)
        box.clear()
        sum_box,ppw=0,0
    return poin


def label_filter(date_awal,date_akhir):
    month_dict = {"1":"Januari","2":"Februari","3":"Maret","4":"April","5":"Mei","6":"Juni"
                 ,"7":"Juli","8":"Agustus","9":"September","10":"Oktober","11":"November","12":"Desember"}
    label_month = []
    label =[]
    obj =  Achievement.objects.filter(date__range=[date_awal,date_akhir])
    for o in obj:
        if o.date.month not in label:
            label.append(str(o.date.month))
        else:
            continue
    label = list(dict.fromkeys(label))
    for l in label:
        label_month.append(month_dict[l])
        for k in range(3):
            label_month.append("")

    return label_month


