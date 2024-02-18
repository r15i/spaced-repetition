import numpy as np
import matplotlib.pyplot as plt



# can be optimized
def oblio_function(time,forgetting_faction, initial_mem=100):
    tmp = initial_mem * (1 - fattore_dimenticanza*0.00045)**time 
    print(tmp)
    return tmp


def calcola_curva_oblio(tempo_trascorso, fattore_dimenticanza, memoria_iniziale):
    memoria = [memoria_iniziale]
    for minuto in tempo_trascorso[1:]:
        memoria_giorno_precedente = memoria[-1]
        memoria.append(oblio_function(minuto,fattore_dimenticanza))
    return memoria

def calcola_curva_oblio_con_ripetizioni(tempo_totale, fattore_dimenticanza, memoria_iniziale=100,soglia=50):
    memoria = [memoria_iniziale]

    i = 0
    while(i<tempo_totale):
        #print(i)
        while(memoria[-1]>soglia):
            memoria_giorno_precedente = memoria[-1]
            
            memoria.append(oblio_function(i,fattore_dimenticanza))
            print(oblio_function(i,fattore_dimenticanza))
            i+=1

        else:
            tempo_totale = tempo_totale-i # elimina i tempi gia' processiati
            i = 0#  ritorna a 0 
            memoria[-1] = memoria_iniziale
            i+=1
    return memoria

# Parametri della curva dell'oblio
n_day = 6
resolution = 60  # Risoluzione in minuti
time_points = n_day  * 24 * 60
time = np.arange(0, time_points, resolution)  # Minuti trascorsi (0 a n_day) con risoluzione specificata

fattore_dimenticanza = 0.5  # Fattore di dimenticanza iniziale [0:1] quanto dimentico 0 ricordo tutto 1 ricordo il massimo possibile in base ai fattori di modello 

# Calcola la curva dell'oblio utilizzando la funzione con NumPy
#memoria = calcola_curva_oblio(time, fattore_dimenticanza)
memoria = calcola_curva_oblio_con_ripetizioni(time_points, fattore_dimenticanza)

# Plot della curva dell'oblio
plt.figure(figsize=(10, 6))
plt.plot(time / 60, memoria, marker='o', label=f'Fattore di dimenticanza {fattore_dimenticanza}')

plt.title('Curva dell\'oblio con risoluzione specificata')
plt.xlabel('Ore trascorse')
plt.ylabel('Memoria residua (%)')
plt.grid(True)
plt.legend()
plt.show()

memoria =[100]


memoria = calcola_curva_oblio_con_ripetizioni(time_points,fattore_dimenticanza)    


# ritorna una lista di indici a partire dalla data di oggi a 2 mesi 
# l'incrementoe' lineare
def calcola_indici_obli(esame,end_date = 60,linear_increase = 1):
    # faccio funzione che calcola un array con numpy
    
    indici = [0]
    j = 0
    i = 0
    red_forgetting_rate = 0.01
    forgetting_rate = 1
    
    while(i<end_date)
        forgetting_rate -= forgetting_rate 
        tmp = oblio_function(j,forgetting_rate)
        if(tmp<50)
            j = 0