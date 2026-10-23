from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl


class URLResponse(BaseModel):
    original_url: HttpUrl
    short_url: str

    class Config:
        from_attributes = True