from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientRead

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=ClientRead, status_code=status.HTTP_201_CREATED)
def create_client(payload: ClientCreate, db: Session = Depends(get_db)):
    exists = db.query(Client).filter(Client.email == payload.email).first()
    if exists:
        raise HTTPException(status_code=409, detail="Client with this email already exists")
    c = Client(name=payload.name, email=payload.email)
    db.add(c)
    db.commit()
    db.refresh(c)
    return ClientRead(id=c.id, name=c.name, email=c.email)

@router.get("/", response_model=list[ClientRead])
def list_clients(db: Session = Depends(get_db)):
    rows = db.query(Client).all()
    return [ClientRead(id=r.id, name=r.name, email=r.email) for r in rows]
