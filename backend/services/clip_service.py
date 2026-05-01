import json
import os
from functools import lru_cache

import numpy as np
import torch
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
from transformers import CLIPModel, CLIPProcessor

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "outfits.json")


@lru_cache
def get_clip():
    model_name = "openai/clip-vit-base-patch32"
    processor = CLIPProcessor.from_pretrained(model_name)
    model = CLIPModel.from_pretrained(model_name)
    model.eval()
    return processor, model


def load_outfits() -> list[dict]:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _encode_texts(texts: list[str]) -> np.ndarray:
    processor, model = get_clip()
    with torch.no_grad():
        inputs = processor(text=texts, return_tensors="pt", padding=True)
        feats = model.get_text_features(**inputs)
    feats = feats / feats.norm(dim=-1, keepdim=True)
    return feats.cpu().numpy()


def _encode_image(image_path: str) -> np.ndarray:
    processor, model = get_clip()
    image = Image.open(image_path).convert("RGB")
    with torch.no_grad():
        inputs = processor(images=image, return_tensors="pt")
        feats = model.get_image_features(**inputs)
    feats = feats / feats.norm(dim=-1, keepdim=True)
    return feats.cpu().numpy()


def recommend_outfits(image_path: str, style: str = "", mood: str = "", weather: str = "", top_k: int = 5):
    outfits = load_outfits()
    prompts = [
        f"{o['style']} {o['mood']} outfit for {o['weather']} weather with {o['color']} tones and {' '.join(o['items'])}"
        for o in outfits
    ]
    text_embeddings = _encode_texts(prompts)
    image_embedding = _encode_image(image_path)

    similarities = cosine_similarity(image_embedding, text_embeddings)[0]
    scored = []
    for outfit, score in zip(outfits, similarities):
        bonus = 0.0
        if style and outfit["style"].lower() == style.lower():
            bonus += 0.07
        if mood and outfit["mood"].lower() == mood.lower():
            bonus += 0.05
        if weather and outfit["weather"].lower() == weather.lower():
            bonus += 0.05
        outfit_copy = dict(outfit)
        outfit_copy["score"] = float(score + bonus)
        scored.append(outfit_copy)

    return sorted(scored, key=lambda x: x["score"], reverse=True)[:top_k]
