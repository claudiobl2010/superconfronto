#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(0, os.path.abspath("%s/.." % os.path.abspath(os.path.dirname(__file__))))

import cherrypy
import logging
import logging.handlers
from superconfronto.rotas import rotas

cherrypy.config.update("%s/superconfronto.conf" % os.path.abspath(os.path.dirname(__file__)))

logging.basicConfig(level=getattr(logging, cherrypy.config['logging.level.superconfronto']))
logger = logging.getLogger()
handler = logging.handlers.TimedRotatingFileHandler(filename=cherrypy.config['logging.path.log.file'], when='midnight', interval=1, backupCount=10)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

d = cherrypy.dispatch.RoutesDispatcher()

for r in rotas:
    d.connect(route=r[0], controller=r[1], action=r[2], name=r[3])

conf = {'/':{'request.dispatch':d},
        '/media':{'tools.staticdir.on':True,
                  'tools.staticdir.root':os.path.abspath(os.path.dirname(__file__)),
                  'tools.staticdir.dir':'media'}
       }

cherrypy.tree.mount(root=None, config=conf)
cherrypy.quickstart()
