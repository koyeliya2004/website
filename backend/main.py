from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.recommendation import router as recommendation_router
from routes.weather import router as weather_router

app = FastAPI(title="AI Fashion Stylist API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommendation_router)
app.include_router(weather_router)


@app.get("/")
def root():
    return {"status": "ok", "service": "ai-fashion-stylist"}
