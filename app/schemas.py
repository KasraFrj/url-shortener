from pydantic import BaseModel , HttpUrl
from datetime import datetime

class URLCreate(BaseModel):
    orginal_url : HttpUrl

class URLResponse(BaseModel):
    short_code : str
    orginal_url : str
    clicks : int
    created_at : datetime

    class Config:
        from_attributes = True