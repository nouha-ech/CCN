def creer_file():
    return []

def est_vide(file):
    return len(file) == 0

def deposer_dans_queue(file, element, priorite):
    timestamp = time.time()
    nouvel_element = [element, priorite, timestamp]
    file.append(nouvel_element)
    return file
def retirer_de_queue(file):
    if est_vide(file):
        return None
    indice_max = 0
    priorite_max = file[0][1]
    timestamp_min = file[0][2]
    for i in range(1, len(file)):
        valeur = file[i][0]
        priorite = file[i][1]
        timestamp = file[i][2]
        if (priorite > priorite_max) or (priorite == priorite_max and timestamp < timestamp_min):
            indice_max = i
            priorite_max = priorite
            timestamp_min = timestamp
    element_retire = file.pop(indice_max)
    return element_retire[0]
    
    
    
    