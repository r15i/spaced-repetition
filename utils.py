
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


class Exam:
    def __init__(self, name = "" ,args = None):
        self.name = name
        if(args == None):
            self.args = []        
        else:
            self.args = args
    

    def set_name(self,name):
        self.name = name
    def set_args(self,args):
        self.args = args
    
    def add_args(self,arg):
        self.args.append(arg)

     
    def get_name(self):
        return self.name         
    def get_args(self):
        return self.args 
    def __str__(self):
        # TO DO 
        pass 



class Arg:
    def __init__(self, name = "" ,k_status = 0. ,n_rep = 0 ,date_last_rep= ""  ):
        self.name = name
        self.k_status = k_status
        self.n_rep = n_rep
        self.date_last_rep = date_last_rep 
        
    def set_name(self,name):
        self.name = name
    def set_k_status(self,k_status):
        self.k_status = k_status
    def set_n_rep(self,n_rep):
        self.n_rep = n_rep
    def set_date_last_rep(self,date_last_rep):
        self.date_last_rep = date_last_rep 

    def get_name(self):
        return self.name
    def get_k_status(self):
        return self.k_status 
    def get_n_rep(self):
        return self.n_rep         
    def get_date_last_rep(self):
        return self.date_last_rep 
    def __str__(self):
        # TO DO 
        pass 

def exam_to_json(exam,filename):
    exam_skel = {
        "name": exam.name,
        "args": []
    }

    for arg in args:
        exam_skel.append({
                "name": arg.name,
                "k": arg.k_status,
                "n_rep": arg.n_rep,
                "date_last_rep": arg.date_last_rep
            })
    

       

# TO DO 
# USED TO ADD PERSISTANCE AT EACH CHANGE
# LOADS ALL THE EXAMS AND MODIFY ONLY THE ONE WE ARE WORKING ON 
# TO DO AFTER 
def update_json(filename,exam):
    pass
    

def parse_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data



def load_exams(filename):   
    # loading exams 
    exams = parse_json(filename)["exams"]
   
    exam_list = []

    for exam in exams:
        
        ex = Exam(exam["name"]) 
        args_list = []
        for argument in exam["args"]:

            arg = Arg()
            arg.set_name(argument["name"])
            arg.set_k_status( argument["k"])
            arg.set_n_rep(argument["n_rep"])
            arg.set_date_last_rep(argument["date_last_rep"])
            
            ex.add_args(arg)
        exam_list.append(ex)
    return exam_list




