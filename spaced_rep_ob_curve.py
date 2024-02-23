import matplotlib.pyplot as plt
import matplotlib 
from math import floor, exp
import json
import numpy as np
from  ob import *
from utils import *



matplotlib.use('Qt5Agg')  # or 'Qt5Agg', 'GTK3Agg', etc.



# Function to plot the a fucntion with associated indexes and value of the function
def plot_function_with_indexes(times, func_val, indexes,h_l = None):
    times = list(range(0, pdays, 1))
    plt.plot(times, func_val, marker="o", linestyle="-")
    
    for index in indexes:
        plt.axvline(
            x=index, color="red", linestyle="--", linewidth=0.5
        )  # Add vertical lines
    
    #to fix for an horziontal line 
    #if h_l is not None:
    #    plt.axvline(y=0.5,color='blue',linestyle='-',linewidth=0.5)
    
    plt.title("Forgetting Curve")
    plt.xlabel("Days")
    plt.ylabel("Retention")
    plt.grid(True)
    plt.show()


def plot_forgetting_curve(in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay):

    times = list(range(0, pdays, 1))

    indexs, retentions = calculate_retention_over_time(
        in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
    )

    plot_function_with_indexes(times,retentions,indexs)





#save_to_json(esame_data, "esami.json")

# tra la data di oggi e la data dell'esame
days = 50  # 2 month to study
risk_factor = 1 / 4  # what fraction of these days to account for problem and ext
dhw = 6  # 6hour of work per day (used to subdive in sessions each argoument)
t_sess = (
    1.30 * 60
)  # length of a session in minutes (this is the main parameter that we can handle for each exam)


in_learn_rate = 0.1  # initial forgetting rate
th_knowledge = (
    0.50  # threshold of when repetion is triggered, how low hour knowledge can go
)
inc_learn_rate = 0.001  # how much we are able to retain more given a repetition (how much the learning rate augment given a session)

under_delay = 4  # initial contiguos time (in session ) used to understand the (Acquisition (),Comprehension, Rielaboration)


#dates till the exam
dates = lista_date(datetime.now(), days)


pdays = round(days- days*risk_factor)

#for some reason the v are one too much



i =  calculate_indexes_over_time(in_learn_rate, pdays, th_knowledge, inc_learn_rate)
v =  calculate_values_over_time(in_learn_rate, pdays, th_knowledge, inc_learn_rate,i)
 
                
#plot function with indexes
plot_function_with_indexes(list(range(0,pdays,1)), v, i,th_knowledge)

#plot_forgetting_curve(in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay)
# Usage:
#exs = parse_json("esami.json")

# for testing select the first
#esame = ex[0]

#print the exam
# for esame in data:
#      print("Title:", esame["title"])
#      print("Topics:", esame["topics"])





# print(indexes)
# print(retentions)
# TO do write the generic version and update
# need also a method to plot have the complete curve


# plot_function_with_indexes

# plot_forgetting_curve(in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay)
# plot_forgetting_curve_with_indexes(
#   in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
# )





















#indici_esame = calcola_indici(Esame,days,risk_factor,dhw,t_sess,in_learn_rate,th_knowledge,inc_lear_rate,under_delay)

# # this goes in calcola indici
# pdays = days - floor(days * risk_factor)  # actual days for preparation

# indexes = calcola_indici_per_argomento(
#     "test", pdays, dhw, t_sess, in_learn_rate, th_knowledge, inc_lear_rate, under_delay
# )

# calculate the indexes for the spaced repetition and the associated retention curve
# this is the bed rock that calculates the indexes for a single part
# indexs, retentions = calculate_retention_over_time(
#     in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
# )
