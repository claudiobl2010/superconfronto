#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from superconfronto.models.base import Base, get_session

class TimeRepository():
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
    criacao = Column('criacao_dt', DateTime)
    ultimo_login = Column('ultimo_login_dt', DateTime)
    qtd_login = Column('qtd_login_num', Integer)
