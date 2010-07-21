#! /usr/bin/python
# -*- coding: utf-8 -*-
import re

def slugify(texto):

    replaces = [["a","á|à|ã|â|ä"],["e","é|è|ê|ë"],["i","í|ì|î|ï"],["o","ó|ò|õ|ô\ö"],["u","ú|ù|û\ü"],["c","ç"]]
       
    # remove espaco em branco do comeco e final
    string = texto.strip()

    if isinstance(string, str):
        string = unicode(string, 'utf8')

    string = string.lower()
    
    # substitui espaco por -
    string = re.sub('\s', '-', string)
    
    for replace in replaces:
        string = re.sub(unicode(replace[1], 'utf8'), replace[0], string)
    
    # remove caracteres invalidos
    string = re.sub('[^a-z0-9\-]', '', string)

    return string
