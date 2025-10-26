import random
def creer_client(numero, date, duree):
    return [numero, date, duree, 0]

def creer_file_clients():
    return []
    
def CreerListeClients():
    nb = int(input("Entrez le nombre de clients : "))
    file = creer_file_clients()
    date = 8 * 3600  #  8 heure * 3600s
    for i in range(1, nb + 1):
        if i == 1:
            intervalle = 0
        else:
            intervalle = random.randint(0, 100)
        date = date + intervalle
        duree = random.randint(0, 150)
        
        client = creer_client(i, date, duree)
        file.append(client)
    return file
    
def convertir_temps(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    return f"{h:02d}h {m:02d}min {s:02d}s"
    
def AfficherFileClients(file):
    print(f"{'Client':<8}{'Arrivée':<20}{'Durée':<15}{'Fin de traitement'}")
    print("-" * 65)
    fin_precedent = 0
    for client in file:
        numero, arrivee, duree, fin = client
        debut = max(arrivee, fin_precedent)
        fin = debut + duree
        client[3] = fin 
        print(f"{numero:<8}"
              f"{convertir_temps(arrivee):<20}"
              f"{str(duree)+'s':<15}"
              f"{convertir_temps(fin)}")
        fin_precedent = fin


file_clients = CreerListeClients()
AfficherFileClients(file_clients)
