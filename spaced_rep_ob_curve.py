from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from math import floor, exp
import json
import numpy as np


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
def calculate_retention_over_time(
    learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
):
    indexs = list(range(0, under_delay))  # initial threshold
    retentions = [1, 1, 1, 1]
    
    while indexs[-1] < pdays:
        print(learn_rate)

        if (
            learn_rate > 0
        ):  # threshold to consider perfect recall (in this case we have almost perfect recal (we forget 0.15)l)

            tmp = indexes[-1] # last session 
            
            #append index new session 
            indexs.append(
                indexs[-1] + round(time_to_reach_retention(learn_rate, th_knowledge))
            )
            #append curve from last to this session 
            retentions = retentions + retention_curve(learn_rate, indexs[-1]-tmp)

            # from the last repetition
            # if disabled is like equally separated
            #learn_rate -= inc_lear_rate
        else:
            retentions.append(1.0)
            

    print(pdays)
    print(indexes)
    print(len(indexes))
    print(retentions)
    print(len(retentions))

    return indexs, retentions


# Function to plot the a fucntion with associated indexes and value of the function
def plot_function_with_indexes(times, func_val, indexs):
    times = list(range(0, pdays, 1))
    indexs, retentions = calculate_retention_over_time(
        learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
    )

    plt.plot(indexs, retentions, marker="o", linestyle="-")
    for index in indexs:
        plt.axvline(
            x=index, color="red", linestyle="--", linewidth=0.5
        )  # Add vertical lines

    plt.title("Forgetting Curve")
    plt.xlabel("Days")
    plt.ylabel("Retention")
    plt.grid(True)
    plt.show()


def plot_forgetting_curve(learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay):

    times = list(range(0, pdays, 1))
    indexs, retentions = calculate_retention_over_time(
        learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
    )

    plt.plot(indexs, retentions, marker="o", linestyle="-")

    plt.title("Forgetting Curve")
    plt.xlabel("Days")
    plt.ylabel("Retention")
    plt.grid(True)
    plt.show()


# ritorna gli indici associati a un singolo argomento se fosse studiato da solo
# uguale a l'altra ma contiene direttamente il numero di giorni calcolati
def calcola_indici_per_argomento(
    arg, pdays, dhw, t_sess, in_learn_rate, th_knowledge, inc_lear_rate, under_delay
):

    # initial understandig phase
    indexs = list(
        range(0, under_delay)
    )  # first days for understanding delay are contiguos

    learn_rate = in_learn_rate

    while indexs[-1] < pdays:
        indexs.append(
            indexs[-1] + round(time_to_reach_retention(learn_rate, th_knowledge))
        )

        if learn_rate > 0:
            learn_rate = learn_rate - inc_lear_rate
            if learn_rate < 0:
                break
    return indexs


# ritorna una lista di indici da oggi alla fine della data dell'esame
# considerando i per ogni argomento una fase contigua di Acquisizione, comprensione e Rielaborazione
# considerando poi una fase di spaced repetition di Applicazione e ricordo
# si procede proseguendo nel programma solo quando 1 si e' conclusa la fase di Acquisizione comrensione e rielaborazione e sono stati trovati degli spazi
# dove inserire nella fase di spaced repetition


# Argomenti
# ex identifica l'esame
# days il numero di giorni a disposizione
# risk_factor quanti di questi giorni saranno effettivamente usati per studiare
# dhw quante ore al giorno possiamo studiare
# t_sess quanto dura al minuto una session ( PARAMETRO PRINCIPALE di ottimizzazione )
# in_learn_rate learning rate iniziale
# th_knowledge threshold sotto il quale non scendere per il learning rate
# inc_learn_rate incremento di learning rate per ogni sessione
# under_delay tempo richiesto in sessioni per comprendere un argomento ed eseguire Acquisizione,Comprensione e Rielaborazione


def calcola_indici(
    ex,
    days,
    risk_factor,
    dhw,
    t_sess,
    in_learn_rate,
    th_knowledge,
    inc_lear_rate,
    under_delay,
):

    pdays = days - floor(days * risk_factor)  # actual days for preparation

    # 1 calcolare gli indici per ogni singolo argomento comprendendo i giorni iniziali di delay
    # calcola_indici_per_argomento(ex,days,risk_factor,dhw,t_sess,in_learn_rate,th_knowledge,inc_lear_rate,under_delay)
    # 2 unire tutti le liste di indici in modo da inserire in ogni gap la fase di understanding
    # 3 identificare ogni sessione con la fase associata per il suo argomento

    indici = [0]  # complete indexes

    return indici


def lista_date(data_inizio=datetime.now(), num_giorni=60):
    date = []
    for i in range(num_giorni):
        data = data_inizio + timedelta(days=i)
        date.append(data)
    return np.array(date)


class Esame:
    def __init__(self, title, topics):
        self.title = title
        self.topics = topics

    def to_dict(self):
        return {"title": self.title, "topics": self.topics}


def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def parse_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


# to save to format
# save_to_json(esame_data, "esami.json")

# Usage:
ex = parse_json("esami.json")[0]


# da modificare per calcolare la differenza
# tra la data di oggi e la data dell'esame


days = 60  # 2 month to study
risk_factor = 1 / 4  # what fraction of these days to account for problem and ext
dhw = 6  # 6hour of work per day (used to subdive in sessions each argoument)
t_sess = (
    1.30 * 60
)  # length of a session in minutes (this is the main parameter that we can handle for each exam)


in_learn_rate = 0.4  # initial forgetting rate
th_knowledge = (
    0.50  # threshold of when repetion is triggered, how low hour knowledge can go
)
inc_lear_rate = 0.001  # how much we are able to retain more given a repetition (how much the learning rate augment given a session)

under_delay = 4  # initial contiguos time (in session ) used to understand the (Acquisition (),Comprehension, Rielaboration)
# shuld be useful

# missing_dates =  # list of date that we missed our session , for each of these dates the overall plan gets shifted in that exact


# print the exam
# for esame in data:
#     print("Title:", esame["title"])
#     print("Topics:", esame["topics"])

# calcolatutte le date da ora fino alla data in oggetto
dates = lista_date(datetime.now(), days)


# indici_esame = calcola_indici(ex,days,risk_factor,dhw,t_sess,in_learn_rate,th_knowledge,inc_lear_rate,under_delay)

# this goes in calcola indici
pdays = days - floor(days * risk_factor)  # actual days for preparation


indexes = calcola_indici_per_argomento(
    "test", pdays, dhw, t_sess, in_learn_rate, th_knowledge, inc_lear_rate, under_delay
)

# calculate the indexes for the spaced repetition and the associated retention curve


# this is the bed rock that calculates the indexes for a single part
""" indexs, retentions = calculate_retention_over_time(
    learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
)
 """

# print(indexes)


# TO do write the generic version and update
# need also a method to plot have the complete curve

# plot_function_with_indexes
plot_forgetting_curve(in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay)
plot_forgetting_curve_with_indexes(
    in_learn_rate, pdays, th_knowledge, inc_lear_rate, under_delay
)
