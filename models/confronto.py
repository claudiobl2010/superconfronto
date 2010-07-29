#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relation
from superconfronto.models.base import Base, get_session, Repository
from superconfronto.models.time import Time

class ConfrontoRepository(Repository):
    pass

class Confronto(Base, ConfrontoRepository):
    
    __tablename__ = 'confronto'
    
    id = Column('confronto_id', Integer, primary_key=True)
    time_casa_id = Column('time_casa_id', Integer, ForeignKey("time.time_id"))
    time_visita_id = Column('time_visita_id', Integer, ForeignKey("time.time_id"))
    time_vencedor_id = Column('time_vencedor_id', Integer, ForeignKey("time.time_id"))
    rodada = Column('rodada_id', Integer)
    data = Column('confronto_dt', DateTime)

    time_casa = relation(Time, primaryjoin=time_casa_id==Time.id)
    time_visita = relation(Time, primaryjoin=time_visita_id==Time.id)
    time_vencedor = relation(Time, primaryjoin=time_vencedor_id==Time.id)
