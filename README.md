# jeu-des-trains

- [jeu-des-trains](#jeu-des-trains)
  - [contenues des applications](#contenues-des-applications)
  - [lancer django](#lancer-django)

## contenues des applications

- jeux_gares : applications pour le jeux des gares
- jeux_lignes : applications pour le jeux des lignes
- ile_de_france_discovery : carte où l'utilisateur pourra renseigner les gares qu'il a déjà visité et téléchargé sa carte des visites

## lancer django

```bash

cd jeu_trains
# lors du premier lancement 
python manage.py makemigrations
python manage.py migrate

# pour lancer le serveur
python manage.py runserver
```
