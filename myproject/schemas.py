from pydantic import BaseModel


class WeatherCreate(BaseModel):
    city: str
    temperature: float

class Weather(WeatherCreate):
    id: int

    class Config:
        orm_mode = True

class ForecastCreate(BaseModel):
    city: str
    date: str
    description: str
    temperature_high: float
    temperature_low: float

class Forecast(ForecastCreate):
    id: int

    class Config:
        orm_mode = True