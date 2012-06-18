# coding: utf-8
#!/usr/bin/env python

import pycurl
import StringIO
import simplejson

def get_status_mercado():
    try:
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, 'http://api.cartola.globo.com/mercado/status.json')
        content_io = StringIO.StringIO()
        curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
        curl.perform()
        response = content_io.getvalue()
        response_dict = simplejson.loads(response)
        return response_dict
    except Exception, e:
        raise e
    finally:
        curl.close()

def get_top_10_times_liga_super_confronto():
    try:
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, 'http://api.cartola.globo.com/liga/super-confronto/rodada/times.json?qtd_itens=10')
        content_io = StringIO.StringIO()
        curl.setopt(pycurl.WRITEFUNCTION, content_io.write)
        curl.perform()
        response = content_io.getvalue()
        response_dict = simplejson.loads(response)
        return response_dict
    except Exception, e:
        raise e
    finally:
        curl.close()
