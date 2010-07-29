#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()

__session__ = None

def get_session():
    global __session__

    if not __session__:
        engine_string = cherrypy.config['database.engine.url']
        pool_size = cherrypy.config['database.engine.pool_size']
    
        engine = create_engine(engine_string, pool_size=pool_size, pool_recycle=120)
        
        __session__ = scoped_session(sessionmaker(bind=engine, autocommit=True, autoflush=False))
    
    return __session__()

class Repository():
    
    def get(self, id):
        session = get_session()
        return session.query(self.__class__).get(id)

    def save(self):
        session = get_session()
        if not self.id: 
            session.add(self)
        session.flush()

    def delete(self):
        session = get_session()
        session.delete(self)
        session.flush()
