# -*- coding: UTF-8 -*-
# import os
# import sys
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BM.settings")
# sys.path.append('/Users/jesusropi/Desktop/Workspace/BM')
from feb.febSoapWrapper import getTemporadasDisponibles, getCategoriasDisponiblesXTemporada, getEquiposInscritosXCategoria, getFasescodCategoria, getGrupos, getJornadas, getPartidos, getPartido, getEstadisticasAcumuladasXEquipo, getEstadisticasAcumuladasXJugador
from feb.febToGCMapper import temporadaItem_to_season, categoriaItem_to_season, equipoItem_to_team, equipoItem_to_teamregistration, faseItem_to_phases, grupoItem_to_team, jornadaItem_to_fixture, partidoItem_to_match, jugador_player, player_team_mapper, infoPartidoItem_to_stats_match_local, infoPartidoItem_to_stats_match_visitor, estadisticaPartidoJugadorItem_player, jugador_player_without_stat
from GC.models import Season, Category, Phase, Group, Fixture, Match, TeamRegistrations,PlayerTeam, Player, Team
#from GC.views import find_player

# Create your views here.

key = ['FEB_Generico']  #Palabra clave para obtencion de datos en servicio web


def find_player(feb_id, nombrecompleto, equipo, partido):   #econtrar player para stat_match_player
    """
        Buscar jugador
        Si feb_id es distinto de 0, buscamos por feb_id.
        Si feb_id es distinto de 0 y no está en BD, crear log.
        Si es igual a cero, buscar por nombre y apellidos
    """
    if feb_id!=0:                                           #filtrar por el id deljugdor, si es distinto de 0
        player = Player.objects.filter(feb_id=feb_id).first()#cogemos ese jugador
        if player == None:                                  #y si no hay ninguno en nuestra base de datos 
            if len(nombrecompleto)>1:                       #si el nobmre completo es mayor que 1
                player = Player.objects.filter(playerteam__team_id=equipo.id).filter(name=nombrecompleto[1]).filter(surname=nombrecompleto[0]).first()  #lo creamos
            else:                                           #si el nombre completo no es mayor que 1
                player = Player.objects.filter(playerteam__team_id=equipo.id).filter(name=nombrecompleto[0]).first()    #lo creamos
            if player==None:                                #y si aun sigue siendo nulo
                fixture = Fixture.objects.get(pk=partido.fixture.id)    #filtramos por jornada
                grupo = Group.objects.get(pk=fixture.group_id)          #filtramos por grupo
                fase = Phase.objects.get(pk=grupo.phase.id)             #filtramos por fase
                team_registration = TeamRegistrations.objects.get(team=equipo, season=fase.season, category=fase.category)  #filtramos por la tabla intermedia entre team y registrations
                player=get_player(team_registration.feb_registration_id, feb_id, estadistica=None)                          #vamos al mappaer a crearlo con os datos del servicio web
        return player   #devolvemos ese jugador
    else:               #si el jugador tiene la id a 0 crearemos ese jugador en nuestra base de datos
        if len(nombrecompleto)>1:
            player = Player.objects.filter(playerteam__team_id=equipo.id).filter(name=nombrecompleto[1]).filter(surname=nombrecompleto[0]).first()
        else:
            player = Player.objects.filter(playerteam__team_id=equipo.id).filter(name=nombrecompleto[0]).first()
        #playerteam = PlayerTeam.objects.filter(team_id=equipo)
        return player


def get_seasons():
    """
        Obtencion de las temporadas 
    """
    response = getTemporadasDisponibles(key)
    for item in response.TemporadasDisponiblesResult[0].TemporadaItems:
        season = temporadaItem_to_season(item)
        season.save()
    return season
        #print "Nombre de temporada:",season.feb_season_id, "\nTemporada:",season.feb_season_name
    #get_category_by_season(Season.objects.all().filter(feb_season_id=2013).first())
#end get_seasons


def get_category_by_season(season):
    """
        Obtencion de categorias por cada temporada, en este caso solo la categoria ORO
    """
    response = getCategoriasDisponiblesXTemporada([season.feb_season_id], key)
    for item in response.CategoriasDisponiblesXTemporadaResult[0].CategoriaItems:
            categoria = Category.objects.get(seasons=season, feb_category_id=item.CategoriaIDs[0])
            category = categoriaItem_to_season(item, season, categoria)
            category.save()                                #Despues de guardar las categorias ponemos el campo season que es un many to many field
            category.seasons = [season]
            category.save()
        #print categorys.name, categorys.feb_category_id, categorys.feb_category_name, categorys.seasons
    #get_teamregistrations_by_category(Category.objects.filter(name='ORO').first(), season)

def get_teamregistrations_by_category(categoria, season):
    """
        Obtencion de los equipos para la categoria ORO
    """
    response = getEquiposInscritosXCategoria([categoria.feb_category_id], key)
    for item in response.EquiposInscritosXCategoriaResult[0].EquipoItems:
        teamregistrations = TeamRegistrations.objects.get(feb_registration_id=item.IdInscripcions[0], category=categoria,season=season)
        team = equipoItem_to_team(item, teamregistrations)
        team.save()                                                 #guradamos el objeto team para despues rellenar la tabla inermedia (many to many field)
        if teamregistrations==None:
            teamRegistrations = equipoItem_to_teamregistration(item, team, categoria, season)
            teamRegistrations.save()
        #print team.feb_team_alias, team.feb_team_name, team.name, teamRegistrations.id
        get_players(teamRegistrations)                              #obtencion de jugadores por equipo
    #get_phase(Season.objects.filter(feb_season_id=2013).first(), Category.objects.filter(name='ORO').first() )

def get_phase(season, categoria):
    """
        Obtencion de fase para la categoria ORO
    """
    response = getFasescodCategoria([season.feb_season_id], [categoria.feb_category_id], key)
    for item in response.FasesResult[0].FaseItems:
        fases = Phase.objects.get(season=season, feb_phase_id=item.FaseIDs[0], category=categoria)
        fase = faseItem_to_phases(item, season, categoria, fases)
        fase.save()
        #print fase.name, fase.feb_phase_alias, fase.feb_phase_id, fase.feb_phase_name, fase.category
        #get_group(fase)
        

def get_group(fase):
    """
        Obtencion del grupo por cada fase
    """
    response = getGrupos([fase.feb_phase_id], key)
    for item in response.GruposResult[0].GrupoItems:
        group = Group.objects.get(phase=fase, feb_group_id=item.GrupoIDs[0])
        grupo = grupoItem_to_team(item, fase, group)
        grupo.save()
        #print grupo.name, grupo.feb_group_id, grupo.feb_group_name, grupo.phase
        #get_jornadas(grupo)


def get_jornadas(grupo):
    """
        Obtencion de cada jornada por cada grupo
    """
    response = getJornadas([grupo.feb_group_id], key)
    for item in response.JornadasResult[0].JornadaItems:
        fixture = Fixture.objects.get(group=grupo, feb_fixture_id=item.IdJornadas[0])
        jornada = jornadaItem_to_fixture(item, grupo, fixture)
        jornada.save()
        #print jornada.feb_fixture_id, jornada.date, jornada.number, jornada.group
        #get_matchs(jornada)


def get_matchs(jornada):
    """
        Obtencion de cada partido de la jornada
    """
    response = getPartidos([jornada.feb_fixture_id], key)   #primero llamamos a los partido para la id
    for item in response.PartidosResult[0].PartidoItems:
        response2 = getPartido(item.IdPartidos, key)        #Despues a cada partido para la jornada indicada
        match = Match.objects.get(feb_match_id=item.IdPartidos[0], fixture=jornada)
        partido = partidoItem_to_match(item, response2.PartidoResult[0], jornada, match)
        partido.save()
        #print partido.feb_match_id, partido.date, partido.visitor_team, partido.local_team, partido.auxiliar_refree, partido.date, partido.fixture, partido.main_refree, partido.place
  
def get_match(jornada, partido):
    """
        Obtencion de cada partido de la jornada
    """
    response = getPartidos([jornada.feb_fixture_id], key)   #primero llamamos a los partido para la id
    for item in response.PartidosResult[0].PartidoItems:
        if item.IdPartidos[0]==partido.feb_match_id:
            response2 = getPartido(item.IdPartidos, key)        #Despues a cada partido para la jornada indicada
            match = Match.objects.get(feb_match_id=partido.feb_match_id, fixture=jornada.id)
            partido = partidoItem_to_match(item, response2.PartidoResult[0], jornada, match)
            partido.save()
           
        
def get_players(teamRegistrations):
    """
        Obtencion de los jugadores de los equipos
    """
    response_team_players = getEstadisticasAcumuladasXEquipo([teamRegistrations.feb_registration_id], key)
    for estadistica_jugador_item in response_team_players.EstadisticasAcumuladasXEquipoResult[0].Jugadoress[0].EstadisticaJugadorItems:
        if estadistica_jugador_item.Nombres[0] != 'Total': 
            player = get_player(teamRegistrations.feb_registration_id, estadistica_jugador_item.IdJugadors[0],estadistica_jugador_item)                      #si es 'total' es la estadistica total de los jugadores, por eso solo cogemos los !=total
            playerteam = player_team_mapper(player, teamRegistrations)
            playerteam.save()
            #print playerteam.player, playerteam.team
    

def get_player(feb_registration_id, id_jugador, estadistica_jugador_item):
    """
        Obtencioon de todos los jugadores a partir de get_players
    """
    if id_jugador!=0:   #si id de jugador es distinto a 0
        response_player = getEstadisticasAcumuladasXJugador([feb_registration_id], [id_jugador], key)
    player = jugador_player(estadistica_jugador_item, estadisticasAcumuladasXJugadorResult = None if id_jugador==0 else response_player.EstadisticasAcumuladasXJugadorResult[0])    #si el id de jugador es 0, estadisticasAcumuladasXJugadorResult es None así se crea en el mapper
    player.save()                       #guadamos al jugador
    #print player.feb_id, player.active, player.teams                
    return player


def get_player_without_stat(feb_registration_id, id_jugador):
    """
        Actualizar el jugador.
    """
    if id_jugador.feb_id!=0:   #si id de jugador es distinto a 0
        response_player = getEstadisticasAcumuladasXJugador([feb_registration_id.feb_registration_id], [id_jugador.feb_id], key)
    #if Player.objects.get(feb_id=id_jugador.id) and Player.objects.get(teams=feb_registration_id.id):
    player = jugador_player_without_stat(id_jugador, feb_registration_id, response_player.EstadisticasAcumuladasXJugadorResult[0] )    #si el id de jugador es 0, estadisticasAcumuladasXJugadorResult es None asi se crea en el mapper
    player.save()                       #guadamos al jugador
    #print player.feb_id, player.active, player.teams                
    return player
    
#get_seasons()#llamar al metodo para ejecutarlos todos los demas en cadena
def get_stat_season(season):
    """
        Obtener temporadas disponibles
    """
    seasons = Season.objects.filter(id=season)
    for season in seasons:
        get_stat_category(season)
    return seasons
def get_stat_category(season):
    """
        Obtener categorias por temporada
    """
    categories=Category.objects.filter(seasons=season)
    for category in categories:
        get_stat_phase(category, season)
    return categories

def get_stat_phase(categoria, season):
    """
        Obtener phase por categoria
    """
    phases = Phase.objects.filter(category=categoria, season=season)
    #print phases
    for phase in phases:
        get_stat_group(phase)
    return phases
    
def get_stat_group(fase):
    """
        Obtener grupo por fase
    """
    groups = Group.objects.filter(phase=fase)
    #print groups
    for group in groups:
        get_stat_fixture(group)
        
    return groups
    
    
def get_stat_fixture(grupo):
    """
        Obtener jornada de grupo
    """
    fixtures = Fixture.objects.filter(group=grupo)
    #print list(fixtures)
    #for fixture in fixtures:
        #get_stat_match(fixture)
    return fixtures
    
    
def get_stat_match(jornada):
    """
        Obtener estadistica de partido y partidos de la jornada
    """
    matchs = Match.objects.filter(fixture=jornada)
    #print 'Jornada:' + str(jornada.number)
    for match in matchs:
        response = getPartido([match.feb_match_id], key)
        #print 'Equipo local:' + str(match.local_team)
        stat_match_team_local = infoPartidoItem_to_stats_match_local(response.PartidoResult[0], match.local_team, match)                #Rellenar campos de esadistica de partido local
        stat_match_team_local.save()
        get_stat_player(response.PartidoResult[0].EstadisticaLocals[0].EstadisticaPartidoJugadorItems, match.local_team, match)         #Rellenar campos de estadistica de jugador local
        #print 'Equipo visitante:' + str(match.visitor_team)
        stat_match_team_visitor = infoPartidoItem_to_stats_match_visitor(response.PartidoResult[0], match.visitor_team, match)          #Rellenar campos de estadistica partido visitante
        stat_match_team_visitor.save()
        get_stat_player(response.PartidoResult[0].EstadisticaVisitantes[0].EstadisticaPartidoJugadorItems, match.visitor_team, match)   #Rellenar campos de estadistica de jugador visitante
    #print [p.visitor_team for p in matchs]
    
    
def get_stat_player(jugadores, equipo, partido):
    """
        Obtener estadisticas de jugadores a partido de jugador, equipo y partido
    """ 
    for jugador in jugadores:
        if jugador.Nombres[0]!='Total':
            nombrecompleto = jugador.Nombres[0].split(', ')
            player = find_player(jugador.IdJugadors[0], nombrecompleto, equipo, partido)
            stat_match_player= estadisticaPartidoJugadorItem_player(jugador, player, partido)   #metodo en models.py para ver si tiene id distinto de 0 y para ver si tiene campos
            stat_match_player.save()
            if jugador.NumeroDorsals[0] != player.dorsal:
                player.dorsal = jugador.NumeroDorsals[0]
                player.save()
        #print jugador
    return stat_match_player
        
    
#get_stat_phase(Category.objects.get(name='ORO'))
#get_stat_match(Fixture.objects.get(pk=31))





"""
    Vistas
"""

from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class ad_estadisticas_form(generic.ListView):
    template_name = 'administration/ad_estadisticas.html'
    def get_queryset(self):
        return Season.objects.order_by('-feb_season_id')[:50]

class ad_objetos_form(generic.ListView):
    template_name = 'administration/ad_objetos.html'
    def get_queryset(self):
        return Season.objects.order_by('-feb_season_id')[:50]


def actualizar_estadistica(request):
#     partidos = request.GET['partido'].split('_')
#     partido_local = partidos[0]
#     partido_visitante = partidos[1]
    #if request.GET['jugador'] == '0':
#     season = Season.objects.filter(id=request.GET['temporada'])
#     categoria = Category.objects.filter(seasons=season)
#     fase = Phase.objects.filter(category=categoria)
#     grupo = Group.objects.filter(phase=fase)
#     jornada = Fixture.objects.filter(group=grupo)
    if (request.GET['action']=="jornada"):
        get_stat_match(Fixture.objects.get(pk=request.GET['jornada']))
    elif (request.GET['action']=="grupo"):
        get_jornadas(Group.objects.get(pk=request.GET['grupo']))
#    partido = Match.objects.filter(fixture=jornada, local_team=partido_local, visitor_team=partido_visitante)
     
    return HttpResponseRedirect(reverse('administrar_e'))
        
def actualizar_objetos(request):
    if (request.GET['action']=='temporada'):
        get_seasons()
    elif (request.GET['action']=='categoria'):
        get_category_by_season(Season.objects.get(id=request.GET['temporada']))
    elif (request.GET['action']=='fase'):
        get_phase(Season.objects.get(id=request.GET['temporada']), Category.objects.get(id=request.GET['categoria']))
    elif (request.GET['action']=='grupo'):
        get_group(Phase.objects.get(id=request.GET['fase']))
    elif (request.GET['action']=='joranda') :
        get_jornadas(Group.objects.get(id=request.GET['grupo']))
    elif (request.GET['action']=='partidos'):
        get_matchs(Fixture.objects.get(id=request.GET['jornada']))
    elif (request.GET['action']=='partido'):
        get_match(Fixture.objects.get(id=request.GET['jornada']), Match.objects.get(feb_match_id=request.GET['partido']))
    elif (request.GET['action']=='equipos'):
        get_teamregistrations_by_category(request.GET['categoria'],request.GET['temporada'])
    elif (request.GET['action']=='jugador'):
        get_player_without_stat(TeamRegistrations.objects.get(team=request.GET['equipo']), Player.objects.get(id=request.GET['jugador']))
        
    return HttpResponseRedirect(reverse('administrar_o'))
        
