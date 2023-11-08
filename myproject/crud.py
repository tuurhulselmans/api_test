from sqlalchemy.orm import Session
from models import Weather

import models
import schemas


def create_weather(db: Session, weather: schemas.WeatherCreate):
    db_weather = Weather(**weather.dict())
    db.add(db_weather)
    db.commit()
    db.refresh(db_weather)
    return db_weather

def get_weathers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Weather).offset(skip).limit(limit).all()

def get_weather(db: Session, weather_id: int):
    return db.query(Weather).filter(Weather.id == weather_id).first()

def create_forecast(db: Session, forecast: schemas.ForecastCreate):
    db_forecast = Forecast(**forecast.dict())
    db.add(db_forecast)
    db.commit()
    db.refresh(db_forecast)
    return db_forecast

def get_forecasts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Forecast).offset(skip).limit(limit).all()

def get_forecast(db: Session, forecast_id: int):
    return db.query(Forecast).filter(Forecast.id == forecast_id).first()