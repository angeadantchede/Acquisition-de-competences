'''
Exercice 4 — Intermédiaire : Deuxième produit matrice × vecteur

Soit

[
B=
\begin{pmatrix}
1 & 0 & 2\
-3 & 4 & 1\
2 & 5 & -2
\end{pmatrix}
]

et

[
y=
\begin{pmatrix}
2\
1\
-1
\end{pmatrix}
]

### Questions

1. Calculer (By) à la main.
2. Vérifier le résultat avec NumPy.
'''
# Là nous allons aborder la deuxième question qui nous demande de vérifier le résultat de la question précédente faites à la main avec Numpy

import numpy as np

B = ([[1, 0, 2],
      [-3, 4, 1],
      [2, 5, -2]])

y = ([2, 1, -1])

result = np.dot(B, y)
print(result)
#On observe que le résultat est pareil, soit [ 0 -3 11]...
