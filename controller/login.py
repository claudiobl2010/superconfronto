#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import *
from superconfronto.utils.cadun import Cadun
from superconfronto.utils.servicos_cartola import ServicosCartola
from superconfronto.models.game import Game
from superconfronto.models.time import Time
from datetime import datetime

class LoginController(BaseController):
    
    def login(self):
        contexto = cherrypy.session.get('contexto')
        if contexto:
            raise cherrypy.HTTPRedirect("/home")

        game = Game().get_game()
        return self.render_to_template("login.html", game=game)

    def autenticacao(self, login, senha):
        
        # Autenticação no Cadun.
        ip = cherrypy.request.remote.ip
        dados_login = Cadun().login(login, senha, ip)
        if not dados_login:
            cherrypy.session.clear()
            return self.render_msg(tipo=self.MSG_ERROR, msg="login e/ou senha não conferem")
            
        # Recupera time no Cartola FC pelo cadun_id.
        cadun_id = dados_login['cadun_id']
        time_cartola = ServicosCartola().get_time_by_cadun_id(cadun_id)
        if not time_cartola:
            cherrypy.session.clear()
            return self.render_msg(tipo=self.MSG_ERROR, msg="primeiro crie seu time no Cartola FC")
            
        # Recupera o time no Super Confronto.
        time_id = time_cartola['id']
        time = Time().get(time_id)
        
        if time:
            time.clube_id = time_cartola['clube_id']
            time.nome = time_cartola['nome']
            time.slug = time_cartola['slug']
            time.nome_cartola = time_cartola['nome_cartola'] 
            time.ultimo_login = datetime.now()
            time.qtd_login = time.qtd_login + 1
            time.save()
            
        contexto = {}
        contexto['dados_login'] = dados_login
        contexto['time_cartola'] = time_cartola
        contexto['time'] = time
        
        cherrypy.session['contexto'] = contexto
            
        return self.render_msg(tipo=self.MSG_SUCCESS, msg="SUCCESS")
