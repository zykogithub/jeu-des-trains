# jeu-des-trains

- [jeu-des-trains](#jeu-des-trains)
  - [contenues des applications](#contenues-des-applications)
  - [configurer Mongodb](#configurer-mongodb)
  - [lancer django](#lancer-django)

## contenues des applications

- jeux_gares : applications pour le jeux des gares
- jeux_lignes : applications pour le jeux des lignes
- ile_de_france_discovery : carte où l'utilisateur pourra renseigner les gares qu'il a déjà visité et téléchargé sa carte des visites

## configurer Mongodb

- lancer le conteneur avec cette commande `docker up -d`
- rentrer dans le conteneur `docker exec -it jeu_trains_mongodb "bash"`
- exectuer la commande `./trim.sh`
- quittez le conteneur

## lancer django

```bash

cd jeu_trains
# lors du premier lancement 
python -m venv env
# sur unix source .bin/activate 
# sur windows .\env\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# pour lancer le serveur
python manage.py runserver
```

Si vous installer des nouvelles dépendances, veuillez les sauvegarder avec la commande `pip freeze > .\requirements.txt`
