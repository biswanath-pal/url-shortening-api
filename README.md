# URL Shortener API

A simple URL Shortener API built with **FastAPI** and **PostgreSQL**.

## Features

- Shorten long URLs
- Redirect using short URLs
- Prevent duplicate URLs
- PostgreSQL database
- FastAPI Swagger documentation

## Tech Stack

- Python 3.14
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

## Project Structure

```
url-shortener-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── utils.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### Clone the project

```bash
git clone <repository-url>
cd url-shortener-api
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment

Create a `.env` file using `.env.example`.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/url_shortener
BASE_URL=http://127.0.0.1:8000
```

### Run the application

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Create Short URL

POST `/shorten`

Request

```json
{
  "url": "https://www.google.com"
}
```

Response

```json
{
  "original_url": "https://www.google.com",
  "short_url": "http://127.0.0.1:8000/AbC123"
}
```

### Redirect

GET `/{short_code}`

Example

```
GET /AbC123
```

Redirects to the original URL.

## Author

Biswanath