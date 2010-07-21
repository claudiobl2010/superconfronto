#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from superconfronto.models.base import Base, get_session

class MensagemRepository():
    pass

class Mensagem(Base, MensagemRepository):
    
    __tablename__ = 'mensagem'
    
    id = Column('mensagem_id', Integer, primary_key=True)
    time_id = Column('time_id', Integer, ForeignKey("time.time_id"))
    mensagem = Column('mensagem_txt', String)
    data = Column('mensagem_dt', DateTime)
    publicado = Column('publicado_bln', String)
