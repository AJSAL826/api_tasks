from db import engine,base
from sqlalchemy import Column,String,Integer



class ticket(base):
    __tablename__="tickets"
    id_no=Column(Integer,primary_key=True)
    gate=Column(String)
    cost=Column(Integer)
    name=Column(String)
