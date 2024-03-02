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
date_list = lista_date(data_inizio=datetime.now(), num_giorni=days_till_exam)
# Create a Calendar object


# list of stuff to do 
day = [time(8, 30, 0),time(10, 0, 0),time(16, 0, 0)]

# LUN MAR MER GIO VEN SAB DOM 
week = [day,day,day,day,day,[],[]] 


"""
week ={}
week["LUN"] = day
week["MAR"] = day
week["MER"] = day
week["GIO"] = day
week["VEN"] = day
week["SAB"] = []
week["DOM"] = []
"""


# loading exams 

exams = parse_json("esami.json")["esami"]


for exam in exams:
    print("Exam:", exam["nome"])
    for argument in exam["argomenti"]:
        print("Argument:", argument["nome"])
        print("K Status:", argument["k"])
        print("Number of Repetitions:", argument["n_rep"])
        print("Date of Last Repetition:", argument["date_last_rep"])
    print()



0





