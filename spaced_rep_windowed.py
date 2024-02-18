from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import json
import numpy as np



# Esempio di utilizzo
# ritorna una lista di indici a partire dalla data di oggi a 2 mesi
# l'incrementoe' lineare


def calcola_indici(end_date=60, linear_increase=1.5):
    # faccio funzione che calcola un array con numpy
    indici = [0]
    tmp_i = 1
    for i in range(0, end_date):
        tmp_i = tmp_i * linear_increase  # increase the next incremetnt

        tmp_i_r = int(np.floor(tmp_i))  # round it to confront it with the back one

        if tmp_i_r >= end_date:
            break

        if tmp_i_r > indici[-1]:
            indici.append(tmp_i_r)  # only if it is more it will increase

    return np.array(indici)


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
#save_to_json(esame_data, "esami.json")


# Usage:
data = parse_json("esami.json")

for esame in data:
    print("Title:", esame["title"])
    print("Topics:", esame["topics"])


# calcolatutte le date da ora fino
dates = lista_date(datetime.now(), 60)

# data incrementata di un giorno
data_ora_futura = datetime.now() + timedelta(days=1)

# calcola della prima parte per poi farne gli offset
indici_esame = calcola_indici(60, 1.1)
window = 1  # finestra tra un primo studio e l'altro


# indici per ogni parte (volendo unc indice di offeset tra le parti)
indici_parte = []
for i, part in enumerate(esame.parti):
    # calcola gli indici per una parte
    # shiftandoli
    indici_parte.append(indici_esame + i * window)


end_date = datetime(2024, 2, 16)  # Sostituisci con la tua data di scadenza


print(esame.nome)
# stampa le varie parti
for i, j in enumerate(dates):
    if j > end_date:  # Verifica se la data e' successiva alla end date
        break  # Interrompi il ciclo se siamo oltre la end date

    print(f"{j.strftime('%Y-%m-%d')}  ", end="\n")

    for k, p in enumerate(esame.parti):
        if i in indici_parte[k]:
            print(f"{p} ", end="\n")

    print("")

