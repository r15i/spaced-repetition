from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from math import floor, exp
import json
import numpy as np
from math import floor, exp


# note thisreturn thesingle value need to modify for multiple


# Formula for forgetting curve: retention = e^(-learn_rate * t)
def retention_curve(learn_rate, times):
    retention = np.exp(-learn_rate * np.array(times))
    return retention


# return the time to reach a target retention (in minutes)
def time_to_reach_retention(learn_rate, target_retention):
    # Utilizziamo la formula inversa della curva di dimenticanza per trovare il tempo necessario
    # t = -ln(retention) / learn_rate
    time_to_reach = -np.log(target_retention) / learn_rate
    return time_to_reach


# return a learning rate for the retention obtained in a certain time (in minutes)
def learning_rate_from_retention(retention, time):
    # Utilizziamo la formula della curva di dimenticanza per trovare il tasso di apprendimento
    # retention = e^(-learn_rate * time)
    learn_rate = -np.log(retention) / time
    return learn_rate




# Function to calculate when to repeat over time (only memorization)
# in_learn_rate initial learning rate
# pdays the number of days
# th_knowledge when to repeat
# inc_learn_rate increase in retention capability
def calculate_indexes_over_time(
        in_learn_rate, pdays, th_knowledge, inc_learn_rate
):
    learn_rate = in_learn_rate
    indexs = [1]
    #while the index of the last idex is lower than the pdays
    while indexs[-1] < pdays:
        if(learn_rate>0):
            #appends the time it will take to reach back to the treshold plus the last repetitiotion index
            indexs.append(indexs[-1]+round(time_to_reach_retention(learn_rate,th_knowledge))) 
            #learn_rate= learn_rate - inc_learn_rate
        else:
            indexs.append(index[-1])

    return indexs

# calculate the curve based on a list of indexes
# (to check if it works with the right logic)
# in_learn_rate initial learning rate
# pdays the number of days
# th_knowledge when to repeat
# inc_learn_rate increase in retention capability
def calculate_values_over_time(
        in_learn_rate, pdays, th_knowledge, inc_learn_rate,indexs
):
    learn_rate = in_learn_rate
    val = [1.0]
    for i in range(1,len(indexs)):
        if(learn_rate>0):
            val = val +list( retention_curve(learn_rate,list(range(indexs[i]-indexs[i-1]))))
            #learn_rate= learn_rate- inc_learn_rate 
        else:
            val.append(1.0)
    return val[:pdays]
 

