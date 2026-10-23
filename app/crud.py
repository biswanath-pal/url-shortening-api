from sqlalchemy.orm import Session
from app import models
from app.utils import generate_short_code


def create_short_url(db: Session, original_url: str):

    # Check if URL already exists
    existing_url = (
        db.query(models.URL)
        .filter(models.URL.original_url == original_url)
        .first()
    )

    if existing_url:
        return existing_url

    while True:
        short_code = generate_short_code()

        existing_code = (
            db.query(models.URL)
            .filter(models.URL.short_code == short_code)
            .first()
        )

        if not existing_code:
            break

    new_url = models.URL(
        original_url=original_url,
        short_code=short_code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url


def get_original_url(db: Session, short_code: str):

    return (
        db.query(models.URL)
        .filter(models.URL.short_code == short_code)
        .first()
    )