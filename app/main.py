from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

from app.database import Base, engine, get_db
from app import models, schemas, crud

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    description="A simple URL Shortener built using FastAPI and PostgreSQL.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "URL Shortener API is running"}

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "message": "The URL Shortener API is running successfully."
    }


@app.post("/shorten", response_model=schemas.URLResponse)
def shorten_url(
    url_data: schemas.URLCreate,
    db: Session = Depends(get_db)
):
    url = crud.create_short_url(
        db,
        str(url_data.url)
    )

    return {
    "original_url": url.original_url,
    "short_url": f"{BASE_URL}/{url.short_code}"
   }


@app.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = crud.get_original_url(
        db,
        short_code
    )

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(url.original_url)