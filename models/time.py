#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relation
from superconfronto.models.base import Base, get_session, Repository
from superconfronto.models.clube import Clube

class TimeRepository(Repository):
    pass

class Time(Base, TimeRepository):
    
    __tablename__ = 'time'
    
    id = Column('time_id', Integer, primary_key=True)
    clube_id = Column('clube_id', Integer, ForeignKey("clube.clube_id"))
    cadun_id = Column('cadun_id', Integer)
    nome = Column('nome_txt', String)
    slug = Column('slug_txt', String)
    nome_cartola = Column('nome_cartola_txt', String)
    nome_pessoa = Column('nome_pessoa_txt', String)
    email = Column('email_txt', String)
    qtd_vitorias = Column('qtd_vitorias_num', Integer)
    qtd_derrotas = Column('qtd_derrotas_num', Integer)
    rodada_entrada = Column('rodada_entrada_id', Integer)
    criacao_cartola = Column('criacao_cartola_dt', DateTime)
    criacao_superconfronto = Column('criacao_superconfronto_dt', DateTime)
    ultimo_login = Column('ultimo_login_dt', DateTime)
    qtd_login = Column('qtd_login_num', Integer)
    
    clube = relation(Clube)
