# Déterminant et rang

Série d’exercices du Chapitre 1 — Algèbre linéaire (bloc B).

Travail : déterminants à la main puis vérification NumPy ; énoncés sur le rang et Gauss.

## Contenu

| Fichier | Niveau | Sujet |
| --- | --- | --- |
| [`exo1.py`](./exo1.py) | Débutant | Déterminant 2×2 — calcul manuel + `np.linalg.det` |
| [`exo2.py`](./exo2.py) | Débutant | Déterminant 3×3 (Sarrus) + vérif NumPy |
| [`exo3.py`](./exo3.py) | Intermédiaire | Rang par échelonnement de Gauss (énoncé) |
| [`exo4.py`](./exo4.py) | Avancé | Élimination de Gauss sans NumPy (énoncé) |
| [`exo5.py`](./exo5.py) | Avancé | Déterminant récursif n×n (énoncé) |

## Ce qui a été travaillé

- Calcul manuel du déterminant 2×2 (`det(A) = 6`) puis contrôle avec NumPy
- Déterminant 3×3 via `np.linalg.det`
- Lecture et préparation des exercices avancés (Gauss, déterminant récursif)

## Lancer un exercice

```bash
cd roadmaps/partie-01-fondations-mathematiques/01-algebre-lineaire/Determinant_Rang
python exo1.py
python exo2.py
```

## Statut

**Terminé** — thème déterminant / rang.
