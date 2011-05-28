#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import cherrypy

from mako.lookup import TemplateLookup
from mako import exceptions

class BaseController():
    
    def render_to_template(self, template, **kw):
        template_dir = '%s/../template' % os.path.abspath(os.path.dirname(__file__))

        lookup = TemplateLookup(directories=[template_dir], 
                                output_encoding='utf-8', 
                                input_encoding='utf-8',
                                default_filters=['decode.utf8'])

        try:
            template = lookup.get_template(template)

            return template.render(**kw)
        except:
            return exceptions.html_error_template().render()