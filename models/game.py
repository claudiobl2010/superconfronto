#! /usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer
from superconfronto.models.base import Base, get_session, Repository

class GameRepository(Repository):
    
    ABERTO = 1
    FECHADO = 2
    EM_ATUALIZACAO = 3
    EM_MANUTENCAO = 4
    LIBERADO_PARA_TESTES = 5
    GAME_OVER = 6

    def get_game(self):
        return self.get(1)

        #session = get_session()
        #game = session.query.filter(self.id == 1).one()
        #return game

class Game(Base, GameRepository):
    
    __tablename__ = 'game'
    
    id = Column('game_id', Integer, primary_key=True)   
    rodada_atual = Column('rodada_atual_num', Integer)
    status_mercado = Column('status_mercado_num', Integer)
