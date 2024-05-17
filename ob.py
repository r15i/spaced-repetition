from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from math import floor, exp
import json
import numpy as np
from math import floor, exp

# baseline ret rate
ret_rate = 1.2 


# MAKE THIS AS A MODEL BASED ON THE USER (retention_curve is the fondamental parameter of the user profile=
def retention_curve( times,k):
    retention = np.exp(-ret_rate*(1-k) * np.array(times))
    return retention


# return the time to reach a target retention (in minutes)
def time_to_reach_retention(target_retention,k):
    # Utilizziamo la formula inversa della curva di dimenticanza per trovare il tempo necessario
    # t = -ln(retention) / ret_rate
    time_to_reach = -np.log(target_retention) / (ret_rate * (1-k))
    return time_to_reach

# used to estimate the k after time number of days  
def k_val_from_retention_time(retention, time):
    k = (np.log(retention) / (time*ret_rate)) + 1 
    return k




