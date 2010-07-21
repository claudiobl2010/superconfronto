#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, DateTime
from superconfronto.models.base import Base, get_session

class AvisoRepository():
    pass

class Aviso(Base, AvisoRepository):
    
    __tablename__ = 'aviso'
    
    id = Column('aviso_id', Integer, primary_key=True)   
    aviso = Column('aviso_txt', String)
    data = Column('aviso_dt', DateTime)
    publicado = Column('publicado_bln', String)
