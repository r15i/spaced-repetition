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


days_till_exam = giorni_tra_date(data_inizio=datetime.now().date(), data_fine=datetime(2024,4,3).date())
#lista giorni da oggi a numero di giorni 
date_list = date_list(data_inizio=datetime.now().date(), num_giorni=days_till_exam)
# Create a Calendar object


# list of stuff to do 
day = [time(8, 30, 0),time(10, 0, 0),time(16, 0, 0)]

# LUN MAR MER GIO VEN SAB DOM 
week = [day,day,day,day,day,[],[]] 

# Define a list of weekdays
weekdays = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]



th_retention = 0.5
k_inc = 0.1
# extimate k_th from how many days we think should pass to add a new argument 
# essentially if there is an argument with a k lower than this means that 
# the number of days to reach the retantion is is less than the number of days 
# given that k defines the forgetting curve is the same for all the days 
# so is not necessary to check for the days remain till to the repetition of
# the argument  but just checking if the k is lower than k_th
k_th = k_val_from_retention_time(th_retention, 6)


# craft the days in wich we work 
# list of the days of the week in wich we work (aka the non empty ones )
# index of days in wich we ork 
work_days = [i for i,x in enumerate(week) if len(x)>0]


# crafting the work_cal with all the dates in wich we study 
# index of the day in the list 
work_cal = []


for i,d in enumerate(date_list):
        #chech wich kind of day is it 
        wd = d.weekday()# days of the week we are considering 
        # if in the list of the days  
        if (wd in work_days):
            work_cal.append(d)

# iterate the arguments untill the the end of the days 


exam = load_exams("esami.json")[1]
# each days ask if the argument has improved 
# check for all the argsk 
# j index in the week and element of the week w 
print(f"Exam Name : {exam.name}")




# if an argument is not started it has null last day of repetition
st_args  = [i for i in exam.args if i.date_last_rep!=None]  #started arguments
new_args  = [i for i in exam.args if i.date_last_rep==None] #new arguments


# final schedule for each day to be used with work_cal
schedule = []

#for all the days in wich we work
# we are considering computing the values at the current day 
for i,sd in enumerate(work_cal):
    
    print(f"\nToday date date\t\t{sd}\n") 
    

    # check if we have days to add another argument
   
    print("checking if there is somenthing to add ") 
    # checker if all arguments have enugh days
    # is assumed that if i have an argument that requires more than a number of days (aka the number of days need to insert a new argument is not worphed adding another one 
    tmp = True 
    for j,a in enumerate(st_args):
        
        print(a.name)
        print(f"date last rep\t\t {a.date_last_rep}")  
        # check if all the arguments repetition is from at least 6 days 
        # to insert a new argument


        # need to check if all arguments have at least 6 days 
        #(int truth we could only check the lowest if we order 
        #the the list of st_args)
        

        if(a.k_status>k_th):
            pass
        else:
            tmp = False
           

    if(tmp == True): 
        #study new arg
        #only do the pop assuming 0 n_rep and k = 0  
        n_arg = new_args.pop()
        print(f"adding : n_arg.name")
        st_args.append(n_arg)



    print("Executing task for the day ")

    day_sched = []
    # Execute the study for the day     
    #for all already studied args 
    for j,a in enumerate(st_args):
        # days since last repetition
        d_from_last =  (sd-a.date_last_rep).days
        print(f"From Last rep {d_from_last}")
        ret_val = retention_curve(times = d_from_last ,k=a.k_status)
        print(f"Value of the ob curve is {ret_val}")
        # if lower of the desired threshold repeat  
        if(ret_val<th_retention):
            # HERE WE NEED TO APPEND TO SOMENTHING THAT WE HAVE STUDIED  
            # A CERTAIN ARGUMENT
            day_sched.append(a)            
            # update the last_rep_to_today 
            a.date_last_rep = sd 
            # increaset the k val  
            a.k_status = a.k_status + k_inc
            # increase the number of repetition 
            a.n_rep = a.n_rep + 1  
    # append how is the day  
    schedule.append(day_sched)
        # doing only the first day to test 
    break#to test first day      
    
    








