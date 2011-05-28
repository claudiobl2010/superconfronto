#! /usr/bin/python
# -*- coding: utf-8 -*-

from superconfronto.controller.index import IndexController

rotas = (
    ['/', IndexController(), 'index', 'index_index'],
)
