# coding: utf-8
#!/usr/bin/env python

import simplejson
import hashlib
from datetime import datetime

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.db.models import Max

from superconfronto.game.models import Game, Liga, LigaTime
from superconfronto.game.resources import *

def home(request):
    now = datetime.now()
    
    game = Game.objects.get(pk=1)
    liga = Liga.objects.get(pk=1)
    ligatime = LigaTime.objects.filter(rodada=game.rodada-1).order_by('posicao')
    ranking_rodada = LigaTime.objects.aggregate(Max('rodada'))['rodada__max']
    
    return render_to_response('home.html', {'game':game, 'liga':liga, 'ligatime':ligatime, 'ranking_rodada':ranking_rodada, 'now':now})

def atualizar(request):
    try:
        key = request.GET.get('key')
    
        if not key or hashlib.md5(key).hexdigest() != '6f389a94d60be020dcb732c9449247df':
            return HttpResponse(simplejson.dumps({'code':401, 'msg':'Unauthorized'}), content_type="application/json; charset=UTF-8")
    
        # Consulta API do Cartola
        status_mercado = get_status_mercado()
        times_liga = get_top_10_times_liga_super_confronto()
        
        # Game
        game = Game.objects.get(pk=1)
        game.rodada = status_mercado['mercado']['rodada']
        game.status = status_mercado['mercado']['status']
        game.fechamento = datetime(year=status_mercado['mercado']['fechamento']['ano'], month=status_mercado['mercado']['fechamento']['mes'], day=status_mercado['mercado']['fechamento']['dia'], hour=status_mercado['mercado']['fechamento']['hora'], minute=status_mercado['mercado']['fechamento']['minuto'], second=0)
        game.atualizacao = datetime.now()
        game.save()
        
        # Liga
        liga = Liga.objects.get(pk=1)
        liga.qtd = times_liga['total']
        liga.save()
        
        # LigaTime
        max_rodada = LigaTime.objects.aggregate(Max('rodada'))
        
        if max_rodada['rodada__max'] < (game.rodada - 1):
            
            for time in times_liga['times']:
                ligatime = LigaTime()
                
                ligatime.posicao = time['posicao']
                ligatime.rodada = game.rodada - 1
                ligatime.pontos_rod = time['pontos_ou_patrimonio']
                ligatime.time_id = time['id']
                ligatime.nome_time = time['nome']
                ligatime.slug_time = time['slug']
                ligatime.nome_cartola = time['nome_cartola']
                ligatime.img_escudo_time_peq = time['imagens_escudo']['img_escudo_32x32']
                ligatime.img_escudo_time_gde = time['imagens_escudo']['img_escudo_160x160']

                ligatime.save()

        return HttpResponse(simplejson.dumps({'code':200, 'msg':'OK'}), content_type="application/json; charset=UTF-8")
    except Exception, e:
        return HttpResponse(simplejson.dumps({'code':500, 'msg':'Internal Error', 'exception':str(e)}), content_type="application/json; charset=UTF-8")
        raise e
