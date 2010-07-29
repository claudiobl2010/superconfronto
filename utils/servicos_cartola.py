#! /usr/bin/python
# -*- coding: utf-8 -*-

import pycurl
import StringIO
import logging
import simplejson

class ServicosCartola():
    
    def get_status_mercado(self):
        try:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, 'http://api.cartola.globo.com/mercado/status.json')
            content_io = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
            curl.perform()
            response = content_io.getvalue()
            response_json = simplejson.loads(response)
            return response_json if not response_json.get('errors') else None
        except Exception, e:
            logging.exception(e)
            raise e
        finally:
            curl.close()

    def get_time_by_time_id(self, time_id):
        try:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, 'http://api.cartola.globo.com/time/id/%s/info.json' % time_id)
            content_io = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
            curl.perform()
            response = content_io.getvalue()
            response_json = simplejson.loads(response)
            return response_json if not response_json.get('errors') else None
        except Exception, e:
            logging.exception(e)
            raise e
        finally:
            curl.close()

    def get_time_by_cadun_id(self, cadun_id):
        try:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, 'http://api.cartola.globo.com/time/cadun/%s/info.json' % cadun_id)
            content_io = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
            curl.perform()
            response = content_io.getvalue()
            response_json = simplejson.loads(response)
            return response_json if not response_json.get('errors') else None
        except Exception, e:
            logging.exception(e)
            raise e
        finally:
            curl.close()

    def get_time_rodada(self, time_id, rodada_id):
        try:
            curl = pycurl.Curl()
            curl.setopt(pycurl.URL, 'http://api.cartola.globo.com/time/id/%s/rodada/%s/info.json' % (time_id, rodada_id))
            content_io = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
            curl.perform()
            response = content_io.getvalue()
            response_json = simplejson.loads(response)
            return response_json if not response_json.get('errors') else None
        except Exception, e:
            logging.exception(e)
            raise e
        finally:
            curl.close()
