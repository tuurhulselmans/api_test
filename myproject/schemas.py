from pydantic import BaseModel


class WeatherCreate(BaseModel):
    city: str
    temperature: float

class Weather(WeatherCreate):
    id: int

    class Config:
        orm_mode = True

