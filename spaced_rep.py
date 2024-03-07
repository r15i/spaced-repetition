import matplotlib.pyplot as plt
import matplotlib
from math import floor, exp
import json
import numpy as np
from ob import *
from utils import *
import calendar
from datetime import datetime, timedelta, time 



cal = calendar.TextCalendar(calendar.SUNDAY)  # Crea un oggetto calendario che inizia la settimana con la domenica

#format is year/month/day
days_till_exam = giorni_tra_date(data_inizio=datetime.now(), data_fine=datetime(2024,4,3))
#lista giorni da oggi a numero di giorni 
date_list = date_list(data_inizio=datetime.now(), num_giorni=days_till_exam)
# Create a Calendar object


# list of stuff to do 
day = [time(8, 30, 0),time(10, 0, 0),time(16, 0, 0)]

# LUN MAR MER GIO VEN SAB DOM 
week = [day,day,day,day,day,[],[]] 

# Define a list of weekdays
weekdays = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]

# faccio un ciclo che controlla 

# list of the dates in wich we work 
schedule = []


# craft the days in wich we work 
# list of the days of the week in wich we work (aka the non empty ones )
# index of days in wich we ork 
work_days = [i for i,x in enumerate(week) if len(x)>0]


# crafting the schedule with all the dates in wich we study 
# index of the day in the list 
for i,d in enumerate(date_list):
        #chech wich kind of day is it 
        wd = d.weekday()# days of the week we are considering 
        # if in the list of the days  
        if (wd in work_days):
            schedule.append(d)

# iterate the arguments untill the the end of the days 


exam = load_exams("esami.json")[1]
# each days ask if the argument has improved 
# check for all the argsk 
# j index in the week and element of the week w 
print(f"{exam.name}")


for i,sd in enumerate(schedule):
    for j,a in enumerate(exam.args):
        print(a.name) 
        print(a.)
        

    
    # compute the ob curve since last repetition to d 
    #ob_curve_val = retention_curve(0,0)
    #if is lower 
    # update the date of the last repetition 
    # increase the k ratio 
    # append the name of the arg to the the date 
    








