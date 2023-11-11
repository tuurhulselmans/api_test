# API Project README

Dit project bevat een eenvoudige API gebouwd met FastAPI, SQLite als database voor persistentie, en een eenvoudige front-end in HTML en JavaScript om met de API te communiceren.

## Inhoudsopgave

- [Projectstructuur](#projectstructuur)
- [Installatie](#installatie)
- [API-endpoints](#api-endpoints)
- [Front-end](#front-end)
- [Bijdragen](#bijdragen)
- [Licentie](#licentie)

## Projectstructuur

De projectstructuur omvat de volgende belangrijke onderdelen:

- `main.py`: Bevat de FastAPI-toepassing en definieert API-endpoints.
- `models.py`: Definieert de database-modellen.
- `crud.py`: Bevat CRUD (Create, Read, Update, Delete) bewerkingen voor de database.
- `schemas.py`: Bevat Pydantic-schemas voor gegevensvalidatie.
- `database.py`: Bevat de configuratie voor de database.
- `static/`: Bevat statische bestanden zoals HTML en JavaScript voor de front-end.

## Installatie

1. Clone de repository:

   ```bash
   git clone https://github.com/jouw-gebruikersnaam/jouw-api-project.git
