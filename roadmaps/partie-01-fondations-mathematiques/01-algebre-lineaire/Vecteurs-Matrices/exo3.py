'''
Exercice 3 — Intermédiaire : Produit matrice × vecteur

Soit la matrice

[
A=
\begin{pmatrix}
2 & 1 & -1\
0 & 3 & 2\
4 & -2 & 1
\end{pmatrix}
]

et le vecteur colonne

[
x=
\begin{pmatrix}
3\
-1\
2
\end{pmatrix}
]

### Questions

1. Calculer à la main le produit

[
Ax
]

2. Vérifier le résultat avec **NumPy** en utilisant :

* l'opérateur `@`
* ou `numpy.dot()`
'''


# Là nous allons aborder la deuxième question qui nous demande de vérifier le trésultat de la question précédente faites à la main avec Numpy en utilisant: l'opérateur @ ou numpy.dot()
import numpy as np

A = np.array([[2, 1, -1],
     [0, 3, 2],
     [4, -2, 1]])

x = np.array([3, -1, 2])
result1 = A @ x
result2 = np.dot(A, x)
print(f"En utilisant l'opérateur @, j'obtiens {result1} et en utilisant numpy.dot, j'obtiens {result2}")

#On observe que le résultat est pareil, soit [ 3  1 16]...
