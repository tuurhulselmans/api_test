from fastapi import Depends, FastAPI, HTTPException
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