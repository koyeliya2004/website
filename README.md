# AI Fashion Stylist (Vercel + Render Deployment)

This repository is configured for **cloud deployment only**:
- **Frontend**: Next.js on **Vercel**
- **Backend**: FastAPI on **Render**

It uses only pre-trained AI (`openai/clip-vit-base-patch32`) and does not train models from scratch.

## Architecture
- `frontend/`: Next.js + Tailwind Pinterest-style UI
- `backend/`: FastAPI API with CLIP-based recommendation, weather endpoint, and saved looks
- `render.yaml`: Render service blueprint for backend
- `vercel.json`: Vercel deployment config for frontend

## Deploy Backend on Render
1. Push this repo to GitHub.
2. In Render, create a new **Web Service** from this repo.
3. Render will auto-detect `render.yaml`.
4. Set environment variables:
   - `OPENWEATHER_API_KEY` (optional)
5. Deploy and copy service URL, e.g.:
   - `https://ai-fashion-stylist-api.onrender.com`

## Deploy Frontend on Vercel
1. Import this repo into Vercel.
2. Set **Root Directory** to `frontend`.
3. Set environment variable in Vercel project:
   - `NEXT_PUBLIC_API_URL=https://<your-render-service>.onrender.com`
4. Deploy.

## Required Environment Variables
### Render (Backend)
- `OPENWEATHER_API_KEY` (optional; mock weather fallback is used if empty)

### Vercel (Frontend)
- `NEXT_PUBLIC_API_URL` (required; must point to your Render backend URL)

## API Endpoints (Render Backend)
- `POST /upload` — Upload image (`multipart/form-data`)
- `POST /recommend` — CLIP outfit retrieval + color palette + style tags
- `GET /weather?city=New York` — Weather info from OpenWeather or mock fallback
- `POST /save-look` — Save outfit
- `GET /saved-looks` — Retrieve saved outfits

## Production Notes
- Ensure CORS is restricted to your Vercel domain before production launch.
- Render free instances can cold start; first recommendation request may be slower.
- CLIP model is downloaded at runtime on first boot if not cached.
