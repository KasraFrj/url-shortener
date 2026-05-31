from sqlalchemy.orm import Session
from . import models
from .redis_client import redis_client
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

def create_short_url(db : Session , orginal_url : str):
    short_code = generate_short_code()

    while db.query(models.URL).filter(models.URL.short_code == short_code).first():
        short_code = generate_short_code()

    db_url = models.URL(original_url = orginal_url , short_code = short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, short_code: str):
    cached_url = redis_client.get(f"url:{short_code}")
    if cached_url:
        return cached_url
    
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if db_url:
        redis_client.setex(f"url:{short_code}", 3600, db_url.original_url)
        db_url.clicks += 1
        db.commit()
        return db_url.original_url
    
    return None
