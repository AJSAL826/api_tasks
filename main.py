from fastapi import FastAPI,Depends
from schema import ticket
from model import base, ticket as model_ticket
from db import engine,Sessions
from sqlalchemy.orm import Session

def get_session():
    session=Sessions()
    try:
        yield session
    finally:
        session.close()

app=FastAPI()
base.metadata.create_all(engine)

@app.get("/ticket")

def tickets(db:Session=Depends(get_session)):
    return db.query(model_ticket).all()



@app.post("/ticket")

def tickets(request:ticket,db:Session=Depends(get_session)):
    detail=model_ticket(gate=request.gate,cost=request.cost,name=request.name)
    db.add(detail)
    db.commit()
    db.refresh(detail)
    return detail

@app.get("/ticket/{id}")


def tickets(id:int, db:Session=Depends(get_session)):
    required=db.query(model_ticket).filter(model_ticket.id_no==id).first()
    return required