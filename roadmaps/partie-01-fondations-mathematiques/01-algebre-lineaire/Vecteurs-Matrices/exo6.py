'''
Exercice 6 — Avancé : Comparaison de performances

Générer deux matrices carrées de taille **200 × 200** contenant des nombres aléatoires.

### Questions

1. Multiplier les deux matrices avec votre fonction précédente.
2. Mesurer le temps d'exécution.
3. Multiplier ensuite les mêmes matrices avec NumPy (`@` ou `np.dot`).
4. Mesurer également le temps d'exécution.
5. Comparer les deux temps obtenus.
6. Expliquer pourquoi NumPy est beaucoup plus rapide.

# Bonus

Écrire une fonction permettant de vérifier si deux matrices peuvent être multipliées.

La fonction devra renvoyer :

* `True` si la multiplication est possible ;
* `False` sinon.

Tester votre fonction avec les couples de dimensions suivants :

* (2×3) et (3×4)
* (4×2) et (3×5)
* (5×5) et (5×1)
* (3×2) et (2×3)
* (2×4) et (2×3)
'''

import random
import numpy as np
import time

# Générrons la Matrice carrées de taille 200 * 200
def generate_matrix(taille):
    return [[random.randint(0, 200) for _ in range(taille)] for _ in range(taille)]

def multiplication_matrices(A, B):
# Puisque nous somme censé avoir compris la logique au niveau de l'exercice 5, nous allons là repprendre ici au lieu de juste copier coller
    m = len(A)
    n1 = len(A[0])
    n2 = len(B)
    p = len(B[0])
    assert n1 == n2, f"Impossible d'effectuer la multiplication entre les deux matrices {n1} et {n2}"
    C = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n1):
                C[i][j] += A[i][k] * B[k][j]
    return C

def main():

    A = generate_matrix(200)
    B = generate_matrix(200)
    debut1 = time.perf_counter()
    result1 = multiplication_matrices(A, B)
    fin1 = time.perf_counter()
    final1 = fin1 - debut1
    #print(result1)

    debut2 = time.perf_counter()
    result2 = np.dot(A, B) # ou result2 = A @ B
    fin2 = time.perf_counter()
    final2 = fin2 - debut2
    #print(result2)

    print(f"{final1} != {final2}")

if __name__ == "__main__":
    main()

#pourquoi NumPy est beaucoup plus rapide.

'''
NumPy est beaucoup plus rapide que mon implémentation, car les calculs sont réalisés par des bibliothèques compilées et hautement optimisées, alors que ma fonction utilise trois boucles Python interprétées.
De plus, NumPy stocke les matrices dans des blocs de mémoire contigus et peut exploiter les optimisations matérielles du processeur.
Ainsi, pour des matrices de grande taille comme 200×200, le temps d'exécution de NumPy est nettement inférieur à celui d'une implémentation Python utilisant des boucles.
'''
