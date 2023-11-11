# API Project README

Dit project is een API die gebouwd is met FastAPI, waarbij gebruik wordt gemaakt van SQLite als database voor persistentie. De API biedt functionaliteit voor het beheren en bekijken van weersvoorspellingen voor specifieke steden.

## Inhoudsopgave

- [Projectstructuur](#projectstructuur)
- [API-endpoints](#api-endpoints)
- [Front-end](#front-end)
- [Screenshots](#screenshots)


## Projectstructuur

De projectstructuur omvat de volgende belangrijke onderdelen:

- `main.py`: Bevat de FastAPI-toepassing en definieert API-endpoints.
- `models.py`: Definieert de database-modellen.
- `crud.py`: Bevat CRUD (Create, Read, Update, Delete) bewerkingen voor de database.
- `schemas.py`: Bevat Pydantic-schemas voor gegevensvalidatie.
- `database.py`: Bevat de configuratie voor de database.
- `static/`: Bevat statische bestanden zoals HTML en JavaScript voor de front-end.


## API-endpoints

- **GET `/users/`**: Haalt de lijst met gebruikers op.
- **GET `/users/{user_id}`**: Haalt een specifieke gebruiker op.
- **POST `/users/`**: Creëert een nieuwe gebruiker.
- **GET `/items/`**: Haalt de lijst met items op.
- **POST `/users/{user_id}/items/`**: Creëert een nieuw item voor een gebruiker.
- **GET `/forecast_ordered/{city}`**: Haalt geordende voorspellingsgegevens op voor een specifieke stad.

Voor meer gedetailleerde informatie over elk endpoint, bekijk de [API-documentatie](http://localhost:8000/docs) tijdens het uitvoeren van de applicatie.

## Screenshots

Voor de werking van de api te laten zien heb ik wat screenshots gemaakt. 

## Front-end

De front-end is een eenvoudige HTML-pagina (`index.html`) met JavaScript (`script.js`).


