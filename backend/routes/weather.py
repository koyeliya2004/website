from fastapi import APIRouter, Query
from services.weather_service import get_weather

router = APIRouter()


@router.get("/weather")
def weather(city: str = Query("New York")):
    return get_weather(city)
