# BackEnd

## Fonctionnalités clés

- Ajout, mise à jour et suppression de produits.

## Installation


### Prérequis

- Python 3.x
- Postgresql

### Instructions

1. Clonez le référentiel depuis GitHub :

   ```bash
   git clone https://github.com/aleo74/ComponentStockAPI
   cd ComponentStockAPI

2. Créez un environnement virtuel (recommandé) :

        python -m venv venv
        source venv/bin/activate  # Pour Linux/macOS
        .\venv\Scripts\activate  # Pour Windows


3. Installez les dépendances Python avec pip :

        pip install -r requirements.txt

4. Configurez les variables d'environnement en copiant, modifiant et en renomant le fichier .env.example en .env à la racine du projet.
Faite la même chose pour .db.env.example si vous utilisez docker.


Assurez-vous de personnaliser les valeurs des variables d'environnement en fonction de votre configuration.
Créer la base de données sous postgres en fonction des configuration du .env

5. Lancez l'application :

        flask run

L'API sera accessible à l'adresse http://127.0.0.1:50001/ .
Utilisez la collection Postman pour tester l'api, ou bien les tests unitaires dans ./tests

#### Docker

executez la commande suivante à la racine du projet :
   
    docker-compose up --build

Vous aurez accès à l'api via les informations renseignées dans .env, et l'accès à PGAdmin