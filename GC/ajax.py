'''
Created on 11/12/2013

@author: jesusropi
'''

from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from GC.models import Category, Phase, Group, Fixture, Match, Season, TeamRegistrations, PlayerTeam


@dajaxice_register
def categoria(request, option):
    dajax = Dajax()
    categorys = Category.objects.filter(seasons=option)
    out = []
    out.append("<option value='0'>Selecciona categoria</option>")
    for option in categorys:
        out.append("<option value='%s'>%s</option>" % (option.id, option.name))
    dajax.assign('#combo2', 'innerHTML', ''.join(out))
    return dajax.json()

@dajaxice_register
def fase(request, option):
    dajax = Dajax()
    season = Season.objects.all().first()
    fases = Phase.objects.filter(category=option)
    out = []
    out.append("<option value='0'>Selecciona fase</option>")
    for option in fases:
        out.append("<option value='%s'>%s</option>" % (option.id, option.name))
    dajax.assign('#combo3', 'innerHTML', ''.join(out))
    return dajax.json()

@dajaxice_register
def grupo(request, option):
    dajax = Dajax()
    grupos = Group.objects.filter(phase=option)
    out = []
    out.append("<option value='0'>Selecciona grupo</option>")
    for option in grupos:
        out.append("<option value='%s'>%s</option>" % (option.id, option.name))
    dajax.assign('#combo4', 'innerHTML', ''.join(out))
    return dajax.json()

@dajaxice_register
def jornada(request, option):
    dajax = Dajax()
    jornadas = Fixture.objects.filter(group=option)
    out = []
    out.append("<option value='0'>Selecciona jornada</option>")
    for option in jornadas:
        out.append("<option value='%s'>%s - %s</option>" % (option.id, option.number, option.date))
    dajax.assign('#combo5', 'innerHTML', ''.join(out))
    return dajax.json()

@dajaxice_register
def partidos(request, option):
    dajax = Dajax()
    partidos = Match.objects.filter(fixture=option)
    out= []
    out.append("<option value=0>Selecciona partido</option>")
    for option in partidos:
        out.append("<option value='%s'>%s - %s</option>" % (option.feb_match_id, option.local_team, option.visitor_team ))
    dajax.assign('#combo6', 'innerHTML', ''.join(out))
    return dajax.json()

# @dajaxice_register
# def partido(request, option):
#     dajax = Dajax()
#     partidos = Match.objects.filter(feb_match_id=option)
#     out= []
#     out.append("<option value=0>Selecciona partido</option>")
#     for option in partidos:
#         out.append("<option value='%s_%s'>%s - %s</option>" % (option.local_team, option.visitor_team, option.local_team, option.visitor_team ))
#     dajax.assign('#combo6', 'innerHTML', ''.join(out))
#     return dajax.json()


@dajaxice_register
def equipo(request, option):
    dajax = Dajax()
    categoria = Category.objects.get(id=option)
    equipo_category = TeamRegistrations.objects.filter(category=categoria)
    out = []
    out.append("<option value=0>Selecciona equipo</option>")
    for option in equipo_category:
        out.append("<option value='%s'>%s</option>" % (option.id, option.team))
    dajax.assign('#combo8', 'innerHTML', ''.join(out))
    return dajax.json()

@dajaxice_register
def jugador(request, option):
    dajax = Dajax()
    player_team = PlayerTeam.objects.filter(team=option)
    out = []
    out.append("<option value=0>Selecciona un jugador</option>")
    for option in player_team:
        out.append("<option value='%s'>%s</option>" % (option.id, option.player))
    dajax.assign('#combo9', 'innerHTML', ''.join(out))
    return dajax.json()

