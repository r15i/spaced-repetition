from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from math import floor, exp
import json
import numpy as np
from math import floor, exp


# note thisreturn thesingle value need to modify for multiple
samp_prec = 1/24 #precision of the sampling by the hour

# Formula for forgetting curve: retention = e^(-forg_rate * t)
def retention_curve(forg_rate, times):
    retention = np.exp(-forg_rate * np.array(times))
    return retention


# return the time to reach a target retention (in minutes)
def time_to_reach_retention(forg_rate, target_retention):
    # Utilizziamo la formula inversa della curva di dimenticanza per trovare il tempo necessario
    # t = -ln(retention) / forg_rate
    time_to_reach = -np.log(target_retention) / forg_rate
    return time_to_reach


# return a learning rate for the retention obtained in a certain time (in minutes)
def learning_rate_from_retention(retention, time):
    # Utilizziamo la formula della curva di dimenticanza per trovare il tasso di apprendimento
    # retention = e^(-forg_rate * time)
    forg_rate = -np.log(retention) / time
    return forg_rate


# Function to calculate when to repeat over time (only memorization)
# in_forg_rate initial learning rate
# pdays the number of days
# th_knowledge when to repeat
# inc_forg_rate increase in retention capability
def calculate_indexes_over_time(in_forg_rate, pdays, th_knowledge, inc_forg_rate):
    forg_rate = in_forg_rate
    indexs = [1]
    k = 0 #initial remembering stauts 

    
    # while the index of the last idex is lower than the pdays
    while indexs[-1] < pdays and len(indexs) < pdays:
        if k < 1:
            forg_rate = forg_rate*(1-k)# update  in the main formula t

            # appends the time it will take to reach back to the treshold plus the last repetitiotion index
            indexs.append(
                indexs[-1] + round(time_to_reach_retention(forg_rate, th_knowledge))
            )

            k = k + inc_forg_rate # update the formula with 1 
        else:
            # no more increase
            indexs.append(indexs[-1])

    # clips
    return indexs


# calculate the curve based on a list of indexes
# (to check if it works with the right logic)
# in_forg_rate initial learning rate
# pdays the number of days
# th_knowledge when to repeat
# inc_forg_rate increase in retention capability
def calculate_values_over_time(
    in_forg_rate, pdays, th_knowledge, inc_forg_rate, indexs
):
    forg_rate = in_forg_rate
    val = []
    k = 0 #initial remembering stauts 
    for i in range(1, len(indexs)):
        # val = val +list( retention_curve(forg_rate,list(range(indexs[i]-indexs[i-1], ) )))
        val.append(1.0)
        val = val + list(
            retention_curve(
                forg_rate, list(np.arange(0,indexs[i] - indexs[i - 1],samp_prec)[1:])
            )
        )
    k = k + inc_forg_rate # update the formula with 1 

    forg_rate = forg_rate*(1-k)# update  in the main formula t
    

        
    return val
