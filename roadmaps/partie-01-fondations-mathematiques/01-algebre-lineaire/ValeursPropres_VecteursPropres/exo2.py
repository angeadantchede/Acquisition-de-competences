'''
Exercice C2 — Polynôme caractéristique (Intermédiaire)
Calculer à la main les valeurs propres, puis les vecteurs propres associés.
A = np.array([[3, 1],
              [2, 2]])
'''
import numpy as np
#Le calcule a étét fait à la main et j'ai onbtenue deux valeurs propres, soit 1 et 4

A = np.array([[3, 1],
              [2, 2]])
val = np.linalg.eig(A)
print(f"Voici le résultat: {val}")
