#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import *

class LogoutController(BaseController):
    
    @logged
    def logout(self, game):
        cherrypy.session.clear()
        raise cherrypy.HTTPRedirect('/')
