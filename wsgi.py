#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(0, os.path.abspath("%s/.." % os.path.abspath(os.path.dirname(__file__))))

import atexit
import cherrypy
import logging
import logging.handlers
from superconfronto.rotas import rotas

cherrypy.config.update({'environment': 'embedded'})

if cherrypy.engine.state == 0:
    cherrypy.engine.start(blocking=False)
    atexit.register(cherrypy.engine.stop)
    
cherrypy.config.update("%s/superconfronto.conf" % os.path.abspath(os.path.dirname(__file__)))

logging.basicConfig(level=getattr(logging, cherrypy.config['logging.level.superconfronto']))
logger = logging.getLogger()
handler = logging.handlers.TimedRotatingFileHandler(filename=cherrypy.config['logging.path.log.file'], when='midnight', interval=1, backupCount=10)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

d = cherrypy.dispatch.RoutesDispatcher()

for r in rotas:
    d.connect(route=r[0], controller=r[1], action=r[2], name=r[3])

conf = {'/':{'request.dispatch': d}}

application = cherrypy.Application(root=None, config=conf)
