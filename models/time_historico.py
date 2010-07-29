#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relation
from superconfronto.models.base import Base, get_session, Repository
from superconfronto.models.time import Time

class TimeHistoricoRepository(Repository):
    pass

class TimeHistorico(Base, TimeHistoricoRepository):
    
    __tablename__ = 'time_historico'
    
    id = Column('time_historico_id', Integer, primary_key=True)
    time_id = Column('time_id', Integer, ForeignKey("time.time_id"))
    ano = Column('ano_num', Integer)
    qtd_vitorias = Column('qtd_vitorias_num', Integer)
    qtd_derrotas = Column('qtd_derrotas_num', Integer)

    time = relation(Time)