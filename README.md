
# Programmation Orienter Objet - JSON – Gestionnaire de fichiers JSON (Console)

Développé par :Debavelaere Mathieu  

- site web :  https://mathieudebavelaere.fr
- Git-hub  :  https://github.com/mathieudebavelaere
- linkedin :  https://www.linkedin.com/in/mathieu-debavelaere-b38825253/
- e-mail   :  mathieu.debavelaere@hotmail.com

---

## Présentation

**Programmation Orienter Objet - JSON** est une application console écrite en Python permettant de gérer dynamiquement des fichiers dans le dossier `.json` :
- Création de fichiers JSON
- Parcours et affichage de données
- Ajout et suppression de clés ou d’objets
- Modification de valeurs
- Filtres par catégories
- Interface terminale colorée et ergonomique

L’objectif est de fournir une interface complète en terminal pour manipuler des structures JSON complexes, notamment des listes d’objets (ex. : jeux vidéo, produits, entrées de catalogue…).

---

## Fonctionnalités principales

- [x] Création d’un fichier JSON
- [x] Parcours de fichiers JSON par clé
- [x] Recherche dynamique (texte ou nombre)
- [x] Filtrage par catégorie
- [x] Ajout de clés avec valeur par défaut
- [x] Renommage de clé
- [x] Suppression d’un objet JSON
- [x] Modification d’une valeur spécifique
- [x] Affichage des fichiers présents dans le dossier `/json`
- [x] Design console (couleurs, encadrés, messages personnalisés)

---

## Arborescence du projet

```
poo_Json/
│
├── main.py                     # Lancement du programme
├── menu_json.py                # Menu principal du programme
├── app_json/                   # Modules de traitement orientés objet
├── tools_json/                 # Fonctions génériques liées aux fichiers JSON
├── tools/                      # Outils utilitaires (affichage, nettoyage console)
└── json/                       # Dossier contenant les fichiers .json manipulés
```

---

## Utilisation

### Lancement
```bash
cd desktop
cd poo_Json
python3 main.py
```

### Navigation
L’utilisateur navigue via un menu principal pour accéder aux différentes fonctions :
1. Créer un fichier JSON
2. Parcourir et rechercher dans un fichier
3. Filtrer par catégories
4. Ajouter une nouvelle clé
5. Créer un nouvel objet
6. Supprimer ou modifier objets/valeurs

---

## Dépendances

- Python ≥ 3.8
- Aucun package externe requis (stdlib uniquement)

---

## Objectif du projet

Ce projet est à la fois un outil pratique pour manipuler des données JSON et une vitrine technique montrant :
- la maîtrise de la POO en Python
- la gestion des erreurs utilisateur
- l’architecture modulaire
- le travail d’interface utilisateur en terminal

---

## Auteur

**Debavelaere Mathieu**  
- site web :  https://mathieudebavelaere.fr
- Git-hub  :  https://github.com/mathieudebavelaere
- linkedin :  https://www.linkedin.com/in/mathieu-debavelaere-b38825253/
- e-mail   :  mathieu.debavelaere@hotmail.com
---

## Licence

Ce projet est distribué à titre personnel et pédagogique.  
N'hésitez pas à le forker, l'adapter ou le contribuer !
