from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas
from database import SessionLocal, engine
import os



if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
allowed_origin = "https://tuurhulselmans.github.io"

app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/weather/", response_model=schemas.Weather)
def create_weather(weather: schemas.WeatherCreate, db: Session = Depends(get_db)):
    return crud.create_weather(db=db, weather=weather)

@app.get("/weather/", response_model=List[schemas.Weather])
def read_weathers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_weathers(db, skip=skip, limit=limit)

@app.get("/weather/{weather_id}", response_model=schemas.Weather)
def read_weather(weather_id: int, db: Session = Depends(get_db)):
    db_weather = crud.get_weather(db, weather_id)
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    return db_weather

@app.delete("/weather/{weather_id}", response_model=schemas.Weather)
def delete_weather(weather_id: int, db: Session = Depends(get_db)):
    db_weather = crud.get_weather(db, weather_id)
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather not found")
    db.delete(db_weather)
    db.commit()
    return db_weather


@app.get("/temperature/{city}", response_model=float)
def get_temperature_by_city(city: str, db: Session = Depends(get_db)):
    weather = crud.get_weather_by_city(db, city)
    if not weather:
        raise HTTPException(status_code=404, detail="Weather data not found for the specified city")

    return weather.temperature


@app.post("/forecast/", response_model=schemas.Forecast)
def create_forecast(forecast: schemas.ForecastCreate, db: Session = Depends(get_db)):
    return crud.create_forecast(db=db, forecast=forecast)

@app.get("/forecast/", response_model=list[schemas.Forecast])
def read_forecasts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_forecasts(db, skip=skip, limit=limit)

@app.get("/forecast/{forecast_id}", response_model=schemas.Forecast)
def read_forecast(forecast_id: int, db: Session = Depends(get_db)):
    db_forecast = crud.get_forecast(db, forecast_id)
    if db_forecast is None:
        raise HTTPException(status_code=404, detail="Forecast not found")
    return db_forecast


@app.get("/forecast_ordered/{city}", response_model=list[schemas.Forecast])
def get_forecast_by_city_ordered_with_temp(
        city: str,
        min_temp: float = None,  # Default value is None
        max_temp: float = None,  # Default value is None
        db: Session = Depends(get_db)
):
    # Get the forecast data for the specified city and order by date
    forecast = crud.get_forecast_by_city_ordered(db, city)

    # Filter forecast data based on min_temp and max_temp if provided
    filtered_forecast = []
    for item in forecast:
        if (min_temp is None or item.temperature_low >= min_temp) and \
                (max_temp is None or item.temperature_high <= max_temp):
            filtered_forecast.append(item)

    if not filtered_forecast:
        raise HTTPException(status_code=404, detail="Forecast data not found for the specified criteria")

    return filtered_forecast


