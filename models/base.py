#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def get_session():
    engine_string = cherrypy.config['database.engine.url']
    pool_size = cherrypy.config['database.engine.pool_size']

    engine = create_engine(engine_string, pool_size=pool_size)
    
    session = sessionmaker(bind=engine, autocommit=True, autoflush=True)
    
    return session()
