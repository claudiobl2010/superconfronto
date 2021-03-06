#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from superconfronto.models.base import Base, get_session, Repository

class ClubeRepository(Repository):
    pass

class Clube(Base, ClubeRepository):
    
    __tablename__ = 'clube'
    
    id = Column('clube_id', Integer, primary_key=True)   
    nome = Column('nome_txt', String)
