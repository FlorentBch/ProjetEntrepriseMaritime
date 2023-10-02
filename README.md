# Cosco Scraping

This student project has to goal to scrap differents informations from the web site cosco shipping line.

## Objectifs

- Scrap the vessels informations (Name, code, flag country,...)
- Schedules port to port for each vessel (name, departure, arrival,...)

## Démarage application

### Set-up environnements variables

Consulter le fichier **option.env.** Changer le nom en **.env** *(pas necéssaire pour le moment (28/08/2023)*

### Docker

docker compose -f "docker-compose.yml" up -d --build

#### Consulter dans docker la base de données

Aller dans le docker de la db -> Terminal -> ```su - postgres``` -> ```psql``` -> *ex :* ```SELECT * FROM cosco.vessel;```
