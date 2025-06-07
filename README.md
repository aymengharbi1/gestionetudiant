# Gestion Etudiant

Cette application fournit un petit outil en ligne de commande pour suivre les informations d'une classe.

## Prérequis

- Python 3

## Utilisation

```bash
# Ajouter un élève
python gestionetudiant.py add-student Prenom Nom "Contact parent"

# Enregistrer une absence
python gestionetudiant.py record-absence <id_eleve> 2024-05-01

# Enregistrer une note
python gestionetudiant.py record-note <id_eleve> Math 15.5

# Afficher les informations d'un élève
python gestionetudiant.py show-student <id_eleve>
```

Les données sont enregistrées dans `gestion.db` (SQLite) à la racine du dépôt.

