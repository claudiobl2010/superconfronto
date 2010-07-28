#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import BaseController

class LogoutController(BaseController):
    
    def logout(self):
        cherrypy.session.clear()
        raise cherrypy.HTTPRedirect('/')
