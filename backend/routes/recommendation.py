import json
import os
import uuid
from fastapi import APIRouter, File, UploadFile, HTTPException

from models.schemas import RecommendationRequest, SaveLookRequest
from services.clip_service import recommend_outfits
from utils.color import extract_color_palette

router = APIRouter()
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploads")
SAVED_LOOKS = os.path.join(os.path.dirname(__file__), "..", "data", "saved_looks.json")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    filename = f"{uuid.uuid4()}-{file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(await file.read())
    return {"image_path": path}


@router.post("/recommend")
def recommend(request: RecommendationRequest):
    if not os.path.exists(request.image_path):
        raise HTTPException(status_code=404, detail="Image not found")
    recommendations = recommend_outfits(request.image_path, request.style, request.mood, request.weather)
    palette = extract_color_palette(request.image_path)
    tags = list({r["style"] for r in recommendations})
    return {"recommendations": recommendations, "style_tags": tags, "color_palette": palette}


@router.post("/save-look")
def save_look(request: SaveLookRequest):
    saved = []
    if os.path.exists(SAVED_LOOKS):
        with open(SAVED_LOOKS, "r", encoding="utf-8") as f:
            saved = json.load(f)
    saved.append(request.look.model_dump())
    with open(SAVED_LOOKS, "w", encoding="utf-8") as f:
        json.dump(saved, f, indent=2)
    return {"message": "saved"}


@router.get("/saved-looks")
def get_saved_looks():
    if not os.path.exists(SAVED_LOOKS):
        return []
    with open(SAVED_LOOKS, "r", encoding="utf-8") as f:
        return json.load(f)
