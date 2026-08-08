'''
Exercice B2 — Déterminant d’une matrice 3×3 par Sarrus (Débutant)
Calculer à la main le déterminant par la règle de Sarrus, puis vérifier avec np.linalg.det.
A = np.array([[2, 1, 3],
              [0, -1, 4],
              [5, 2, 1]])
'''

import numpy as np

A = np.array([[2, 1, 3],
              [0, -1, 4],
              [5, 2, 1]])

determinant = np.linalg.det(A)
print(f"Le déterminant de A est égale à {determinant}")
