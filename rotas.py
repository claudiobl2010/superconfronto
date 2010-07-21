#! /usr/bin/python
# -*- coding: utf-8 -*-

from superconfronto.controller.home import HomeController

rotas = (
    ['/', HomeController(), 'index', 'home_index'],
    ['/login', HomeController(), 'login', 'home_login'],

    ['/teste', HomeController(), 'teste', 'home_teste'],
    ['/teste2/{nome}', HomeController(), 'teste2', 'home_teste2'],
    ['/teste3', HomeController(), 'teste3', 'home_teste3'],
)
