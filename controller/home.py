#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import *

class HomeController(BaseController):
    
    @authenticated
    def home(self, game, time):
        return self.render_to_template("home.html")
