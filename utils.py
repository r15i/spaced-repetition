

# ritorna una lista di indici da oggi alla fine della data dell'esame
# considerando i per ogni argomento una fase contigua di Acquisizione, comprensione e Rielaborazione
# considerando poi una fase di spaced repetition di Applicazione e ricordo
# si procede proseguendo nel programma solo quando 1 si e' conclusa la fase di Acquisizione comrensione e rielaborazione e sono stati trovati degli spazi
# dove inserire nella fase di spaced repetition
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
pass


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

#print the exam
for esame in data:
     print("Title:", esame["title"])
     print("Topics:", esame["topics"])

