"""
Il modulo datetime fornisce l'oggetto time, simile all'oggetto Tempo di questo capitolo,
ma che contiene un ricco insieme di metodi e operatori. 

1. Usate il modulo datetime per scrivere un programma che ricavi la data odierna e visualizzi 
il giorno della settimana.

2. Scrivete un programma che riceva una data di nascita come input e visualizzi l'età dell'utente 
e il numero di giorni, ore, minuti e secondi che mancano al prossimo compleanno.

3. Date due persone nate in giorni diversi, esiste un giorno in cui uno ha un'età doppia dell'altro.
Questo è il loro "Giorno del Doppio". 
Scrivete un programma che prenda due date di nascita e calcoli quando si verifica il "Giorno del Doppio".

4. Un pò più difficile: scrivetene una versione più generale che calcoli il giorno in cui una persona 
ha n volte l'età di un'altra.
"""

from datetime import datetime, timedelta

#1
oggi = datetime.now()
giorno_settimana = oggi.strftime("%A")

print("Oggi è il", oggi.strftime("%d/%m/%Y"), "e il giorno della settimana è", giorno_settimana)

#2
# inserisci la data di nascita dell'utente nel formato "aaaa-mm-gg"
data_nascita = datetime.strptime(input("Inserisci la data di nascita (aaaa-mm-gg): "), "%Y-%m-%d")
oggi = datetime.now()

# calcola l'età dell'utente
eta = oggi.year - data_nascita.year - ((oggi.month, oggi.day) < (data_nascita.month, data_nascita.day))

# calcola la data del prossimo compleanno
compleanno = datetime(oggi.year, data_nascita.month, data_nascita.day)
if compleanno < oggi:
    compleanno = datetime(oggi.year + 1, data_nascita.month, data_nascita.day)

# calcola il tempo che manca al prossimo compleanno
tempo_restante = compleanno - oggi

# calcola i giorni, le ore, i minuti e i secondi del tempo che manca al prossimo compleanno
giorni = tempo_restante.days
ore = int(tempo_restante.seconds / 3600)
minuti = int((tempo_restante.seconds % 3600) / 60)
secondi = tempo_restante.seconds % 60

# visualizza i risultati
print("L'età dell'utente è", eta, "anni.")
print("Il prossimo compleanno è il", compleanno.strftime("%d/%m/%Y"), "e mancano ancora", giorni, "giorni,", ore, "ore,", minuti, "minuti e", secondi, "secondi.")

# 3
# input della data di nascita come stringa
data_str = input("Inserisci la data di nascita della prima persona nel formato gg/mm/aaaa: ")

# parsing della data
compleanno = datetime.strptime(data_str, "%d/%m/%Y")

# input della seconda data di nascita come stringa
data2_str = input("Inserisci la data di nascita della seconda persona nel formato gg/mm/aaaa: ")

# parsing della seconda data
compleanno2 = datetime.strptime(data2_str, "%d/%m/%Y")

# calcolo della differenza di età in giorni
differenza_eta = abs(compleanno - compleanno2)
giorni_differenza = differenza_eta.days

# calcolo del Giorno del Doppio
if compleanno > compleanno2:
    giorno_doppio = compleanno + timedelta(days=giorni_differenza)
else:
    giorno_doppio = compleanno2 + timedelta(days=giorni_differenza)

# output della data del Giorno del Doppio
print("Il Giorno del Doppio è il", giorno_doppio.strftime("%d %B %Y"))

# 4
# input delle date di nascita come stringhe
data1_str = input("Inserisci la data di nascita della prima persona nel formato gg/mm/aaaa: ")
data2_str = input("Inserisci la data di nascita della seconda persona nel formato gg/mm/aaaa: ")

# input del fattore di età
fattore_eta = float(input("Inserisci il fattore di età (es. 2 per calcolare il giorno in cui una persona ha 2 volte l'età dell'altra): "))

# parsing delle date
compleanno1 = datetime.strptime(data1_str, "%d/%m/%Y")
compleanno2 = datetime.strptime(data2_str, "%d/%m/%Y")

# calcolo della differenza di età in giorni
differenza_eta = abs(compleanno1 - compleanno2)
giorni_differenza = differenza_eta.days

# calcolo del Giorno del Fattore
if compleanno1 > compleanno2:
    giorno_fattore = compleanno1 + timedelta(days=int(giorni_differenza * fattore_eta))
else:
    giorno_fattore = compleanno2 + timedelta(days=int(giorni_differenza * fattore_eta))

# output della data del Giorno del Fattore
print(f"Il Giorno del Fattore è il {giorno_fattore.strftime('%d %B %Y')}")