#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import simplejson
import cherrypy

from mako.lookup import TemplateLookup
from mako import exceptions

from superconfronto.models.game import Game
from superconfronto.models.time import Time

class BaseController():
    
    MSG_ERROR = -1
    MSG_AVISO = 0
    MSG_SUCCESS = 1
    
    def render_to_template(self, template, **kw):
        template_dir = '%s/../template' % os.path.abspath(os.path.dirname(__file__))

        lookup = TemplateLookup(directories=[template_dir], 
                                output_encoding='utf-8', 
                                input_encoding='utf-8',
                                default_filters=['decode.utf8'])

        try:
            template = lookup.get_template(template)

            return template.render(**kw)
        except:
            return exceptions.html_error_template().render()

    def render_to_json(self, data):
        cherrypy.response.headers['Content-Type'] = "application/json; charset=utf-8"
        return simplejson.dumps(data)
    
    def render_msg(self, tipo=MSG_AVISO, msg=None):
        return self.render_to_json({'tipo':tipo, 'msg':msg})

def authenticated(fn):
    def authenticated_fn(self, *args, **kw):
        game = Game.get_game()

        if game.status_mercado in [Game.EM_ATUALIZACAO, Game.EM_MANUTENCAO, Game.LIBERADO_PARA_TESTES]:
            raise cherrypy.HTTPRedirect("/")
        
        contexto = cherrypy.session.get('contexto')
        if not contexto:
            raise cherrypy.HTTPRedirect("/")
        
        time = contexto.get('time')
        if not time:
            raise cherrypy.HTTPRedirect("/")

        return fn(self, game=game, time=time, *args, **kw)

    return authenticated_fn
    
def logged(fn):
    def logged_fn(self, *args, **kw):
        game = Game.get_game()

        if game.status_mercado in [Game.EM_ATUALIZACAO, Game.EM_MANUTENCAO, Game.LIBERADO_PARA_TESTES]:
            raise cherrypy.HTTPRedirect("/")

        contexto = cherrypy.session.get('contexto')
        if not contexto:
            raise cherrypy.HTTPRedirect("/")

        time = contexto.get('dados_login')
        if not time:
            raise cherrypy.HTTPRedirect("/")

        return fn(self, game=game, *args, **kw)

    return logged_fn
