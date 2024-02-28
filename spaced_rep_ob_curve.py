import matplotlib.pyplot as plt
import matplotlib
from math import floor, exp
import json
import numpy as np
from ob import *
from utils import *



matplotlib.use("Qt5Agg")  # or 'Qt5Agg', 'GTK3Agg', etc.


# Function to plot the a fucntion with associated indexes and value of the function
def plot_function_with_indexes(func_val, indexes, h_l=None):
    
    #time axis from the function
    times = list(range(0, len(func_val), 1))
    plt.plot(times, func_val, marker="o", linestyle="-")

    for index in indexes:
        plt.axvline(
            x=index*samp_prec, color="red", linestyle="--", linewidth=0.5
        )  # Add vertical lines

    # to fix for an horziontal line
    if h_l is not None:
        plt.hlines(
            y=h_l, xmin=0, xmax=len(times), color="blue", linestyle="-", linewidth=1.5
        )

    plt.title("Forgetting Curve")
    plt.xlabel("Days")
    plt.ylabel("Retention")
    plt.grid(True)
    plt.show()


def plot_forgetting_curve(
    in_forg_rate, pdays, th_knowledge, inc_lear_rate, under_delay
):

    times = list(range(0, pdays, 1))

    indexs, retentions = calculate_retention_over_time(
        in_forg_rate, pdays, th_knowledge, inc_lear_rate, under_delay
    )

    plot_function_with_indexes(times, retentions, indexs)


# tra la data di oggi e la data dell'esame
days = 7  # 2 month to study
risk_factor = 1 / 4  # what fraction of these days to account for problem and ext
in_forg_rate = 1.2  #initial forgetting rate (based on the concept that after 1 day we forget 70% if what we have learned)(this is were we have the calibration)
                    #to calibrate tells how much we remeber after a day (is better as a worst case (it is a faster))
inc_forg_rate = 0.1 # how much we are able to retain more given a repetition (how much the learning rate augment given a session)(also here) expressed between 0-1
                     # wich means that 0 we had no improvement 1 we have maximumum recall
th_knowledge = (
    0.30  # threshold of when repetion is triggered, how low hour knowledge can go
)

under_delay = 4  # initial contiguos time (in session ) used to understand the (Acquisition (),Comprehension, Rielaboration)


# dates till the exam
dates = lista_date(datetime.now(), days)


pdays = round(days - days * risk_factor)

# for some reason the v are one too much
i = calculate_indexes_over_time(in_forg_rate, pdays, th_knowledge, inc_forg_rate)
v = calculate_values_over_time(in_forg_rate, pdays, th_knowledge, inc_forg_rate, i)





# plot function with indexes
plot_function_with_indexes(v, i, th_knowledge)

