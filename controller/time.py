#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import *
from datetime import datetime
from superconfronto.models.clube import Clube

class TimeController(BaseController):
    
    @logged
    def cadastro(self, game):
        
        contexto = cherrypy.session.get('contexto')
        
        time_cartola = contexto.get('time_cartola')
        time = contexto.get('time')
        
        temporada = datetime.now().strftime('%Y')
        
        clube = Clube().get(time_cartola['clube_id'])

        return self.render_to_template("cadastro.html", 
                                       time_cartola=time_cartola, 
                                       time=time, 
                                       temporada=temporada, 
                                       clube=clube)
