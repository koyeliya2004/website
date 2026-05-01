from pydantic import BaseModel
from typing import List


class RecommendationRequest(BaseModel):
    image_path: str
    style: str = ""
    mood: str = ""
    weather: str = ""


class OutfitRecommendation(BaseModel):
    id: int
    style: str
    mood: str
    weather: str
    color: str
    items: List[str]
    image: str
    score: float


class SaveLookRequest(BaseModel):
    look: OutfitRecommendation


class WeatherResponse(BaseModel):
    city: str
    weather: str
    temperature_c: float
