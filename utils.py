
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





