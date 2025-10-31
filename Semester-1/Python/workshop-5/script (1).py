import numpy.random as rd

def simul_X():
    x = rd.random()
    if x < 1/3:
        return "PILE"
    else:
        return "FACE"

resultat = simul_X()
print(f"Résultat: {resultat}")
n_simulations = 1000000
resultats = [simul_X() for _ in range(n_simulations)]
    
pile_fois = resultats.count("PILE")
face_fois = resultats.count("FACE")
    
print(f"\nSur {n_simulations} simulations:")
print(f"PILE: {pile_fois} fois ({pile_fois/n_simulations:.2%})")
print(f"FACE: {face_fois} fois ({face_fois/n_simulations:.2%})")



