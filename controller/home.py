#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import BaseController
from superconfronto.utils.slug import slugify
from superconfronto.utils.cadun import Cadun
from superconfronto.utils.servicos_cartola import ServicosCartola

class HomeController(BaseController):
    
    def index(self):
        if cherrypy.session.get('contexto'):
            return self.render_to_template("home.html")
        else:
            return self.render_to_template("login.html")
        
    def login(self, login, senha):
        ip = cherrypy.request.remote.ip
        
        dados_login = Cadun().login(login, senha, ip)
        
        if dados_login:
            contexto = {}
            
            contexto['dados_login'] = dados_login
                     
            #1) Vai no servico Cartola que busca um time pelo Cadun_ID.
            #2) Se falhar o login falha tmb (Usuario esta associado ao servico 438 porem ainda nao montou time no Cartola).
            #3) Com os dados recuperados do item 1 recupera o time.
            #4) Se item 3 falhar e porque usuario nao tem cadastro no super confronto.
            #5) Se 3 = ok atualiza informacoes do time e coloca o time no contexto.
                     
            cherrypy.session['contexto'] = contexto
            
            import pdb; pdb.set_trace()
            
            aa = ServicosCartola().get_status_mercado()
            bb = ServicosCartola().get_time_by_cadun_id(contexto['dados_login']['cadun_id'])
            cc = ServicosCartola().get_time_by_time_id(3421862)
            dd = ServicosCartola().get_time_rodada(3421862, 10)
            ee = ServicosCartola().get_time_rodada(3421862, 11)
            ff = ServicosCartola().get_time_rodada(3421862, 12)
            

            return self.render_msg(tipo=self.MSG_SUCCESS, msg="SUCCESS")
        else:
            return self.render_msg(tipo=self.MSG_ERROR, msg="ERROR")
            
    def teste(self):
        
        ip = cherrypy.request.remote.ip
        
        user_data = Cadun().autenticacao('cartolafc2010', '123abc123', '187.13.61.200')
        
        slug = slugify('Boladão Silvá FC')
        
        a = {'nome':'Claudio', 'atletas':['pedro','joao','marcos'], 'flag_t': True, 'flag_f': False, 'obj_none': None, 'cadun_id': 1254221, 'slug': slug, 'user_data': user_data}
        return self.render_to_json(a)

    def teste2(self, **kw):
            return self.render_to_template("teste2.html", nome=kw['nome'])

    def teste3(self, **kw):
        data = {'nome':kw['nome'], 'sobrenome':kw['sobrenome'], 'lista': [10, 20, 30, 40, 50]}
        return self.render_to_json(data)
