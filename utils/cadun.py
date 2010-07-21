#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
import pycurl
import StringIO
import logging

class Cadun():

    def login(self, login, senha, ip):
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
            
            match = re.search(".*\<usuarioAutenticado\>.*\<glbId\>(?P<glbId>.+)\</glbId\>.*\<login\>(?P<login>.+)\</login\>.*\<status\>AUTENTICADO\</status\>.*\<usuarioID\>(?P<usuarioID>[0-9]+)\</usuarioID\>.*\</usuarioAutenticado\>.*", response)
            if match:
                match_dict = match.groupdict()
                
                dados_login ={}
                dados_login['login'] = match_dict['login']
                dados_login['glbid'] = match_dict['glbId']
                dados_login['cadun_id'] = int(match_dict['usuarioID'])
                
                return dados_login
        except Exception, e:
            logging.exception(e)
        finally:
            curl.close()
               
        return None
