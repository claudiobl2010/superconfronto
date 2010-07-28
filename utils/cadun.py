#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import pycurl
import StringIO
import logging

class Cadun():

    def autenticar(self, login, senha, ip):
        try:
            curl = pycurl.Curl()
            
            curl.setopt(pycurl.URL, 'https://autenticacao.globo.com/ws/rest/autenticacao')
            curl.setopt(pycurl.PORT, 443)
            
            curl.setopt(pycurl.HTTPHEADER, ["Content-type: text/xml"])
    
            curl.setopt(pycurl.POST, 1)        
            curl.setopt(pycurl.POSTFIELDS, '<usuarioAutenticado><glbId></glbId><login>%s</login><senha>%s</senha><ip>%s</ip></usuarioAutenticado>' % (login, senha, ip))
            
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            
            content_io = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
            
            curl.perform()
            
            response = content_io.getvalue()
            
            match = re.search(".*\<usuarioAutenticado\>.*\<glbId\>(?P<glbId>.+)\</glbId\>.*\<status\>AUTENTICADO\</status\>.*\</usuarioAutenticado\>.*", response)
            if match:
                match_dict = match.groupdict()

                return match_dict['glbId']

        except Exception, e:
            logging.exception(e)
        finally:
            curl.close()
               
        return None

    def autorizar(self, glbid, ip):
        try:
            curl = pycurl.Curl()
            
            curl.setopt(pycurl.URL, 'https://autenticacao.globo.com/ws/rest/autorizacao')
            curl.setopt(pycurl.PORT, 443)
            
            curl.setopt(pycurl.HTTPHEADER, ["Content-type: text/xml"])
    
            curl.setopt(pycurl.POST, 1)        
            curl.setopt(pycurl.POSTFIELDS, '<usuarioAutorizado><glbId>%s</glbId><ip>%s</ip><servicoID>438</servicoID></usuarioAutorizado>' % (glbid, ip))
            
            curl.setopt(pycurl.SSL_VERIFYPEER, 0)
            
            content_io = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
            
            curl.perform()
            
            response = content_io.getvalue()
            
            match = re.search(".*\<usuarioAutorizado\>.*\<glbId\>(?P<glbId>.+)\</glbId\>.*\<status\>AUTORIZADO\</status\>.*\<usuarioID\>(?P<usuarioID>[0-9]+)\</usuarioID\>.*\</usuarioAutorizado\>.*", response)
            if match:
                match_dict = match.groupdict()
                
                dados_login ={}
                dados_login['glbid'] = match_dict['glbId']
                dados_login['cadun_id'] = int(match_dict['usuarioID'])
                
                return dados_login
        except Exception, e:
            logging.exception(e)
        finally:
            curl.close()
               
        return None
    
    def login(self, login, senha, ip):
        glbid = self.autenticar(login, senha, ip)

        if glbid:
            dados_login = self.autorizar(glbid, ip)
            return dados_login
        
        return None
