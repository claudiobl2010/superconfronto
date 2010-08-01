#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import *

class TimeController(BaseController):
    
    @logged
    def cadastro(self, game):
        return self.render_to_template("cadastro.html")
