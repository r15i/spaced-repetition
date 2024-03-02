
from datetime import datetime, timedelta
import json
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from math import floor, exp
import json
import numpy as np
from math import floor, exp

# calcola la lista delle date dalla data di inizio a num_giorni
def lista_date(data_inizio=datetime.now(), num_giorni=60):
    date = []
    for i in range(num_giorni):
        data = data_inizio + timedelta(days=i)
        date.append(data)
    return np.array(date)

# calcola i giorni tra due date
def giorni_tra_date(data_inizio=datetime.now(), data_fine=datetime.now()):
    return (data_fine - data_inizio).days


class Arg:
    def __init__(self, name = "" ,k_status = 0. ,n_rep = 0 ,date_last_rep= "00-00-00"  ):
        self.name = name
        self.k_status = k_status
        self.n_rep = n_rep
        self.date_last_rep = date_last_rep 
        
    def set_name(name):
        self.name = name
    def set_k_status(k_status):
        self.k_status = k_status
    def set_n_rep(n_rep):
        self.n_rep = n_rep
    def set_date_last_rep(date_last_rep):
        self.date_last_rep = date_last_rep 

    def get_name(name):
        return name
    def get_k_status(k_status):
        return k_status 
    def get_n_rep(n_rep):
        return n_rep         
    def get_date_last_rep(date_last_rep):
        return date_last_rep 
    def __str__(self):
        # TO DO 
        pass 

def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def parse_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def load_args(filename):   
    # loading exams 
    exams = parse_json(filename)["esami"]
   
    obj_exam  = []

    for exam in exams:
        print("Exam:", exam["nome"])
        ex = Arg()
        
        for argument in exam["argomenti"]:
            print("Argument:", argument["nome"])
            ex.set_name = argument["nome"]
            print("K Status:", argument["k"])
            ex.set_k_status = argument["k"]
            print("Number of Repetitions:", argument["n_rep"])
            ex.set_n_rep = argument["n_rep"]
            print("Date of Last Repetition:", argument["date_last_rep"])
            ex.set_date_last_rep=argument["date_last_rep"]
        print()
        obj_exam.append(ex)

    return obj_exam




