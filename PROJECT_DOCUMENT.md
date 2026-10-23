# URL Shortener API Assessment

## Project Overview

This project is a URL Shortener API developed using FastAPI and PostgreSQL.

### Features

- Generate short URLs
- Redirect to original URLs
- Prevent duplicate entries
- Store data in PostgreSQL

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

## How to Run

1. Create a virtual environment.
2. Install requirements.
3. Create a PostgreSQL database named `url_shortener`.
4. Configure `.env`.
5. Run:

```bash
uvicorn app.main:app --reload
```

6. Open:

```
http://127.0.0.1:8000/docs
```

## Endpoints

### POST /shorten

Creates a short URL.

### GET /{short_code}

Redirects to the original URL.

## Notes

The project follows a modular structure and uses SQLAlchemy ORM for database operations.