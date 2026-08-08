'''
Exercice B1 — Déterminant d’une matrice 2×2 (Débutant)
Calculer à la main le déterminant, puis vérifier avec NumPy.
A = np.array([[4, 7],
              [2, 5]])
'''

import numpy as np

#Le calcule est déjà fait à la main et j'ai obtenue que det(A) = 6
#Là mtn on nous demande de vérifier avec Numpy...

A = np.array([[4, 7],
              [2, 5]])

#Pour calculer le déterminant, on utilise les fonction de la lib linalg, on obtien donc ce qui suit

determinant = np.linalg.det(A)
print (f"Le déterminant de A est égale à {determinant}")

#On obtient effectivement det(A) = 6.0 donc c'est parfait...
