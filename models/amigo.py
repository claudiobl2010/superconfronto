#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relation
from superconfronto.models.base import Base, get_session, Repository
from superconfronto.models.time import Time

class AmigoRepository(Repository):
    pass

class Amigo(Base, AmigoRepository):
    
    __tablename__ = 'amigo'
    
    id = Column('amigo_id', Integer, primary_key=True)
    time_id = Column('time_id', Integer, ForeignKey("time.time_id"))
    time_amigo_id = Column('time_amigo_id', Integer, ForeignKey("time.time_id"))
    data = Column('amigo_dt', DateTime)
    
    time = relation(Time, primaryjoin=time_id==Time.id)
    time_amigo = relation(Time, primaryjoin=time_amigo_id==Time.id)
