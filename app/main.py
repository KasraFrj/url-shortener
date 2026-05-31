from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener")

@app.post("/shorten")
def shorten_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_short_url(db, str(url.orginal_url))

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    orginal_url = crud.get_url_by_code(db, short_code)
    if not orginal_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=orginal_url)

@app.get("/stats/{short_code}")
def get_stats(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if not db_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return db_url