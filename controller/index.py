#! /usr/bin/python
# -*- coding: utf-8 -*-

import cherrypy

from superconfronto.controller.base import *

class IndexController(BaseController):
    
    def index(self):
        return self.render_to_template("index.html")
