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


# Function to calculate retention over time
#
def calculate_retention_over_time(
    learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
):
    indexs = list(range(0, under_delay))  # initial threshold
    retentions = [1, 1, 1, 1]

    while indexs[-1] < pdays:
        print(learn_rate)

        if (
            learn_rate
            > 0  # threshold to consider perfect recall (in this case we have almost perfect recal (we forget 0.15)l)
        ):

            # append index new session
            indexs.append(
                indexs[-1] + round(time_to_reach_retention(learn_rate, th_knowledge))
            )

            # append the new part of the curve from time before
            retentions = retentions + retention_curve(
                learn_rate, indexs[-1] - indexs[-2]
            )

            # from the last repetition
            # if disabled is like equally separated
            # learn_rate -= inc_lear_rate
        else:
            retentions.append(1.0)

    print(pdays)
    print(indexs)
    print(len(indexs))
    print(retentions)
    print(len(retentions))

    return indexs, retentions
