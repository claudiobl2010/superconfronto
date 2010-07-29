#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import BaseController

class HomeController(BaseController):
    
    def home(self):
        return self.render_to_template("home.html")
