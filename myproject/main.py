from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

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
