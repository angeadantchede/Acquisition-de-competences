'''
Exercice 5 — Avancé : Multiplication de matrices sans NumPy

Considérons les matrices

[
A=
\begin{pmatrix}
2 & 1 & 3\
0 & -1 & 4
\end{pmatrix}
]

et

[
B=
\begin{pmatrix}
1 & 5\
2 & 0\
-1 & 3
\end{pmatrix}
]

### Questions

1. Écrire une fonction Python nommée `multiplication_matrices(A, B)` qui multiplie deux matrices sans utiliser NumPy.
2. Utiliser uniquement des listes Python et des boucles `for`.
3. Vérifier que le résultat obtenu est correct.
'''
import numpy as np

def multiplication_matrices(A, B):
    m = len(A)
    n = len (A[0])
    n1 = len (B)
    p = len (B[0])
    assert n == n1, f"Impossible de faire la multiplication entre {n}  et {n1}"
    print("Puisque tout est bon alors oui on peut lancer les calculs")
    C = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():
    A = ([[2, 1, 3],
      [2, 1, 3],
      [3, 2, 1]])

    B = ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]])

    C = np.array([[2, 1, 3],
          [2, 1, 3],
          [3, 2, 1]])

    D = np.array([[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]])
    resultat = multiplication_matrices(A, B)
    print("Résultat de ma fonction :")
    print(resultat)
    print("Voyons voir si tu as tout fait comme il faut en vérifiant avec Numpy")
    result = np.dot(C, D)
    print(result)

if __name__ == "__main__":
    main()


'''
Si toi tu culapabilise parceque tu n'as pas vite conpris la logique derrirère ou même que tu as perdu du temps pour comprendre, sache que c'était pareil chez moi.
J'ai passé 2 jour à y travailler, comprendre les choses comme il faut, comprendre les syntaxe, ce que retourne les fonctions, la différence de syntaxe en présence de bibliothèque et aussi en absence de bibliothèque.
C'était fustrant de ne pas avoir faire ça en 30min mais c'est bien normal parce que je n'ai pas l'habitude de m'appliquer alors, oui c'est l'objectif, apprendre encore, encore et encore. Et continuer malgré les éhecs...
'''
