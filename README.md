# Gestion des élèves

Cette application permet à un enseignant de gérer les informations de ses élèves via une interface en ligne de commande.

## Prérequis

- Python 3.12

## Utilisation

```bash
python3 main.py add "Alice" 12 15.0   # Ajoute un élève
python3 main.py list                    # Liste les élèves
python3 main.py update 1 --grade 16.0   # Met à jour un élève
python3 main.py remove 1                # Supprime un élève
```

Les données des élèves sont stockées dans le fichier `students.json`.
