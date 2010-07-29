#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, Float
from sqlalchemy.orm import relation
from superconfronto.models.base import Base, get_session, Repository
from superconfronto.models.time import Time

class TimeRodadaRepository(Repository):
    pass

class TimeRodada(Base, TimeRodadaRepository):
    
    __tablename__ = 'time_rodada'
    
    id = Column('time_rodada_id', Integer, primary_key=True)
    time_id = Column('time_id', Integer, ForeignKey("time.time_id"))
    rodada = Column('rodada_id', Integer)
    pontos = Column('pontos_num', Float)
    qtd_vitorias = Column('qtd_vitorias_num', Integer)
    qtd_derrotas = Column('qtd_derrotas_num', Integer)

    time = relation(Time)