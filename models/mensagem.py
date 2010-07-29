#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relation
from superconfronto.models.base import Base, get_session, Repository
from superconfronto.models.time import Time

class MensagemRepository(Repository):
    pass

class Mensagem(Base, MensagemRepository):
    
    __tablename__ = 'mensagem'
    
    id = Column('mensagem_id', Integer, primary_key=True)
    time_id = Column('time_id', Integer, ForeignKey("time.time_id"))
    mensagem = Column('mensagem_txt', String)
    data = Column('mensagem_dt', DateTime)
    publicado = Column('publicado_bln', String)

    time = relation(Time)
