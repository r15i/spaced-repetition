import numpy as np
import matplotlib.pyplot as plt



# can be optimized
def oblio_function(time,forgetting_faction, initial_mem=100):
    return initial_mem * (fattore_dimenticanza*0.00045)**time 


def calcola_curva_oblio(tempo_trascorso, fattore_dimenticanza, memoria_iniziale):
    memoria = [memoria_iniziale]
    for minuto in tempo_trascorso[1:]:
        memoria_giorno_precedente = memoria[-1]
        memoria.append(oblio_function(minuto,fattore_dimenticanza))
    return memoria

# Parametri della curva dell'oblio
n_day = 1
resolution = 60  # Risoluzione in minuti
time = np.arange(0, n_day  * 24 * 60, resolution)  # Minuti trascorsi (0 a n_day) con risoluzione specificata

fattore_dimenticanza = 0.01  # learning rate(how well i learn) [1:0.01]
memoria_iniziale = 100  # Memoria iniziale

# Calcola la curva dell'oblio utilizzando la funzione con NumPy
memoria = calcola_curva_oblio(time, fattore_dimenticanza, memoria_iniziale)

# Plot della curva dell'oblio
plt.figure(figsize=(10, 6))
plt.plot(time / 60, memoria, marker='o', label=f'Fattore di dimenticanza {fattore_dimenticanza}')

plt.title('Curva dell\'oblio con risoluzione specificata')
plt.xlabel('Ore trascorse')
plt.ylabel('Memoria residua (%)')
plt.grid(True)
plt.legend()
plt.show()




