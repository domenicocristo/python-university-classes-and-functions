"""
Scrivete una funzione di nome moltiplica_tempo che accetti un oggetto Tempo e un numero, 
e restituisca un nuovo oggetto Tempo che contiene il prodotto del Tempo iniziale per il numero.

Usate poi moltiplica_tempo per scrivere una funzione che prenda un oggetto Tempo che rappresenta 
il tempo finale di una gara, e un numero che rappresenta la distanza percorsa, e restituisca un 
oggetto Tempo che rappresenta la media di gara (tempo al chilometro).
"""

class Tempo:
    # Metodo costruttore, che inizializza i valori di ore, minuti e secondi e controlla che siano plausibili
    def __init__(self, ore, minuti, secondi):
        if not (0 <= ore < 24 and 0 <= minuti < 60 and 0 <= secondi < 60):
            raise ValueError("I valori di ore, minuti e secondi devono essere plausibili")
        self.ore = int(ore)
        self.minuti = int(minuti)
        self.secondi = int(secondi)
    
    # Metodo di rappresentazione a stringa dell'oggetto Tempo, che restituisce una stringa nel formato "hh:mm:ss"
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.ore, self.minuti, self.secondi)
    
def moltiplica_tempo(t, num):
    # Controllo che l'oggetto tempo sia di tipo Tempo e che il numero sia un intero o un float
    if not isinstance(t, Tempo) or not isinstance(num, (int, float)):
        raise TypeError("L'oggetto tempo deve essere di tipo Tempo e il numero deve essere un intero o un float")
    # Calcolo il tempo totale in secondi moltiplicando i secondi, i minuti e le ore dell'oggetto Tempo per il numero
    tot_secondi = (t.ore * 3600 + t.minuti * 60 + t.secondi) * num
    # Divido il tempo totale in ore, minuti e secondi
    ore, resto = divmod(tot_secondi, 3600)
    minuti, secondi = divmod(resto, 60)
    # Restituisco un nuovo oggetto Tempo con i valori di ore, minuti e secondi calcolati
    return Tempo(int(ore), int(minuti), int(secondi))

def media_gara(tempo_finale, distanza):
    # Controllo che l'oggetto tempo_finale sia di tipo Tempo e che la distanza sia un intero o un float
    if not isinstance(tempo_finale, Tempo) or not isinstance(distanza, (int, float)):
        raise TypeError("L'oggetto tempo_finale deve essere di tipo Tempo e la distanza deve essere un intero o un float")
    # Calcolo il tempo medio per km chiamando la funzione moltiplica_tempo con il tempo finale e l'inverso della distanza
    tempo_per_km = moltiplica_tempo(tempo_finale, 1 / distanza)
    # Restituisco il tempo medio per km
    return tempo_per_km

tempo_finale = Tempo(1, 30, 0) 
distanza = 10  

tempo_medio_per_km = media_gara(tempo_finale, distanza)

print("Tempo medio per km: ",tempo_medio_per_km) 