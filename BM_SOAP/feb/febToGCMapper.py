'''
Created on 02/12/2013

@author: jesusropi
'''

from GC.models import Season, Category, Team, Phase, Group, Fixture, Match, StatsMatchTeam, Player, StatsMatchPlayer, PlayerTeam, TeamRegistrations
from datetime import datetime 


def temporadaItem_to_season(temporadaItem):
    """
        Obtencion de las temporadas
    """
    season = Season.objects.get(feb_season_id=temporadaItem.TemporadaIDs[0])
    if season == None:
        season = Season()
    season.feb_season_id = temporadaItem.TemporadaIDs[0]
    season.feb_season_name = temporadaItem.TemporadaNombres[0]
    season.name = temporadaItem.TemporadaNombres[0]
    return season
    
    
def categoriaItem_to_season(categoriaItem, season, category):
    """
        Obtencion de la categoria ORO por la temporada
    """
    if category==None:
        category = Category()
    category.name = categoriaItem.CategoriaNombres[0]
    category.feb_category_id = categoriaItem.CategoriaIDs[0]
    category.feb_category_name = categoriaItem.CategoriaNombres[0]
    return category


def equipoItem_to_team(equipoItem, teamregistrations):
    """
        Obtencion de los equipos inscritos en la categoria ORO
    """
    if teamregistrations==None:
        team = Team()
    team.name = equipoItem.NombreEquipos[0]
    team.feb_team_name = equipoItem.NombreEquipos[0]
    team.feb_team_alias = equipoItem.AliasEquipos[0]
    return team


def equipoItem_to_teamregistration(equipoItem, team, categoria, season):
    """
        Rellenar objeto intermedio del equipo
    """
    teamregistration = TeamRegistrations()
    teamregistration.feb_registration_id = equipoItem.IdInscripcions[0]
    teamregistration.team = team
    teamregistration.category = categoria
    teamregistration.season = season
    return teamregistration


def faseItem_to_phases(faseItem, season, category, phase):#Modificar esto por la base de datos cambiada. 
    """
        Obtencion de la fase segun la categoria, en este caso, ORO y season
    """
    #phase = Phase.objects.get(category=category, season=season)
    if phase == None:
        phase=Phase()
        phase.category = category
        phase.season = season
    phase.name = faseItem.FaseNombres[0]
    phase.feb_phase_id = faseItem.FaseIDs[0]
    phase.feb_phase_name = faseItem.FaseNombres[0]
    phase.feb_phase_alias = faseItem.FaseAliass[0]
    return phase


def grupoItem_to_team(grupoItem, fase, group):
    """
         Obtencion del grupo segun la fase
    """
    #group = Group.objects.get(phase=fase)
    if group== None:
        group = Group()
        group.phase = fase
    group.name = grupoItem.GrupoNombres[0]
    group.feb_group_id = grupoItem.GrupoIDs[0]
    group.feb_group_name = grupoItem.GrupoNombres[0]
    return group


def jornadaItem_to_fixture(jornadaItem, grupo, fixture):
    """
        Obtencion de la jornada segun el grupo perteneciente
    """
    #fixture = Fixture.objects.get(group=grupo)
    if fixture==None:
        fixture = Fixture()
        fixture.group = grupo
    fixture.feb_fixture_id = jornadaItem.IdJornadas[0]
    fixture.date = datetime.strptime(jornadaItem.FechaJornadas[0],"%d/%m/%Y")   #rellenar campo date con ese formato
    fixture.number = jornadaItem.NumJornadas[0]
    return fixture


def infoPartidoItem_to_match(infoPartidoItem, jornada, match=None ):            #si no existe el partido lo creamos
    """
        Obtencion de informacion del partido segun la jornada y el id del partido
    """
    if match == None:
        match = Match()
        match.fixture = jornada
        match.visitor_team = TeamRegistrations.objects.filter(feb_registration_id=infoPartidoItem.IdInscripVisitantes[0]).first().team      #para obtener el id de partido del objeto team y teamregistrations
        match.local_team = TeamRegistrations.objects.filter(feb_registration_id=infoPartidoItem.IdInscripLocals[0]).first().team
    match.date = datetime.strptime(infoPartidoItem.Fechas[0],"%d/%m/%Y")
    match.main_refree = infoPartidoItem.ArbitroPrincipals[0]
    match.auxiliar_refree = infoPartidoItem.ArbitroAuxiliars[0]
    match.place = infoPartidoItem.Campos[0]
    return match


def partidoItem_to_match(partidoItem, infoPartidoItem, jornada, match):
    """
        Obtencion de los partidos
    """
    #match = Match.objects.get(fixture=jornada)
    if match==None:
        match = Match()
    match.feb_match_id = partidoItem.IdPartidos[0]
    infoPartidoItem_to_match(infoPartidoItem, jornada, match)                #llamar a esta funcion para coger la informacion 
    return match


def jugador_player(estadistica_jugador_item, estadisticasAcumuladasXJugadorResult):
    """
        Obtencion del jugador por el partido
    """
    player = Player()
    player.feb_id = estadistica_jugador_item.IdJugadors[0]
    player.active = True #campo boolean
    if estadistica_jugador_item!= None and estadistica_jugador_item.IdJugadors[0]==0:                              #si el id de jugador es igual a 0 solo pondremos nombre y apellidos
        name = estadistica_jugador_item.Nombres[0]
        name= name.split(', ')                                                 #aqui solo usaremos estadistica_jugador_item
        player.name = name[1]                                                  #el otro es para la estadistica que no podremos poner
        player.surname = name[0]                                               #a causa de id=0, lo buscabamos en estadistica por equipo
        surname=name[0].split(' ')                                             #con el id, si id==0 no busca y no contiene nada
        player.surname_1 = surname[0]
        if len(surname)>1:
            player.surname_2 = surname[1]
    else:                                                                       #si el jugador tiene id!=0 pondra mas cosas a parte del nombre y los apellidos, las estadisticas del jugador
        player.name = estadisticasAcumuladasXJugadorResult.Nombres[0]
        player.surname = estadisticasAcumuladasXJugadorResult.Apellidoss[0]     # son los dos apellido, para guardar por separado:
        separado = player.surname.split(' ')                                    #hacemos separacion de variables cuando haya un espacio
        player.surname_1 = separado[0]                                          #y lo guardamos
        if len(separado) >1:                                                    #si no hay segundo apellido
            player.surname_2 = separado[1]
        player.born_date = datetime.strptime(estadisticasAcumuladasXJugadorResult.FechaNacs[0],"%d/%m/%Y")
        player.photo = estadisticasAcumuladasXJugadorResult.URLs[0]
    return player
    

def jugador_player_without_stat(player, id_registration, estadisticasAcumuladasXJugadorResult):
    """
        Actualizar solo un jugador en concreto.
    """
    if player==None:
        player.feb_id=estadisticasAcumuladasXJugadorResult.IdJugadors[0]
        player.teams = id_registration.id_registration
    player.active = True #campo boolean                                                                       #si el jugador tiene id!=0 pondra mas cosas a parte del nombre y los apellidos, las estadisticas del jugador
    player.name = estadisticasAcumuladasXJugadorResult.Nombres[0]
    player.surname = estadisticasAcumuladasXJugadorResult.Apellidoss[0]     # son los dos apellido, para guardar por separado:
    separado = player.surname.split(' ')                                    #hacemos separacion de variables cuando haya un espacio
    player.surname_1 = separado[0]                                          #y lo guardamos
    if len(separado) >1:                                                    #si no hay segundo apellido
        player.surname_2 = separado[1]
    player.born_date = datetime.strptime(estadisticasAcumuladasXJugadorResult.FechaNacs[0],"%d/%m/%Y")
    player.photo = estadisticasAcumuladasXJugadorResult.URLs[0]
    return player
    
def player_team_mapper(player, teamRegistrations):
    """
        rellenar objeto intermedio de jugador y equipo
    """
    playerteam = PlayerTeam()
    playerteam.player = player
    playerteam.team = teamRegistrations.team
    return playerteam


def trayectoriaItem_player(TrayectoriaItem):
    pass


def equipoClasificacionItem_team():
    pass


def estadisticaEquipo_to_match():
    pass


def estadisticaJugadorItem_player(estadisticaJugadorItem):
    pass
    

def infoPartidoItem_to_stats_match_local(infoPartidoItem, partidolocal, partido):
    """
        Estadisticas del equipo local
    """
    statsmatchteam = StatsMatchTeam.objects.filter(match=partido).get(team=partidolocal)    #Filtramos por partido y por equipo y obtenemos esa isntancia
    if statsmatchteam==None:                                                                #Si no esxiste la instancia se crea
        statsmatchteam = StatsMatchTeam()                                                   #con las claves foraneas
        statsmatchteam.team = partidolocal                                                  #Si no existe la instancia entonces solo actualiza los campos
        statsmatchteam.match = partido
        
    statsmatchteam.score = infoPartidoItem.ResultadoLocals[0]
    statsmatchteam.partial_scores = infoPartidoItem.ParcialesLocals[0]
    statsmatchteam.first_partial = infoPartidoItem.PrimerParcialLocals[0]
    statsmatchteam.second_partial = infoPartidoItem.SegundoParcialLocals[0]
    statsmatchteam.third_partial = infoPartidoItem.TercerParcialLocals[0]
    statsmatchteam.four_partial = infoPartidoItem.CuartoParcialLocals[0]
    statsmatchteam.extended_time = infoPartidoItem.ProrrogasLocals[0]
    statsmatchteam.number_extended_times = infoPartidoItem.NumeroProrrogass[0]
    return statsmatchteam
    
    
def infoPartidoItem_to_stats_match_visitor(infoPartidoItem, partidovisitante, partido):
    """
        Estadisticas del equipo visitantae
    """
    
    statsmatchteam = StatsMatchTeam.objects.filter(match=partido).get(team=partidovisitante)    
    if statsmatchteam==None:
        statsmatchteam = StatsMatchTeam()
        statsmatchteam.team = partidovisitante
        statsmatchteam.match = partido

    statsmatchteam.score = infoPartidoItem.ResultadoVisitantes[0]
    statsmatchteam.partial_scores = infoPartidoItem.ParcialesVisitantes[0]
    statsmatchteam.first_partial = infoPartidoItem.PrimerParcialVisitantes[0]
    statsmatchteam.second_partial = infoPartidoItem.SegundoParcialVisitantes[0]
    statsmatchteam.third_partial = infoPartidoItem.TercerParcialVisitantes[0]
    statsmatchteam.four_partial = infoPartidoItem.CuartoParcialVisitantes[0]
    statsmatchteam.extended_time = infoPartidoItem.ProrrogasVisitantes[0]
    statsmatchteam.number_extended_times = infoPartidoItem.NumeroProrrogass[0]
    return statsmatchteam


def estadisticaPartidoJugadorItem_player(estadisticaPartidoJugadorItem, jugador, partido):
    """
        Estadisticas del jugaodor 
    """
    
    statsmatchplayer = StatsMatchPlayer.objects.filter(match=partido).get(player=jugador)
    if statsmatchplayer==None:
        statsmatchplayer = StatsMatchPlayer()
        statsmatchplayer.player = jugador
        statsmatchplayer.match = partido
        
    statsmatchplayer.seconds = estadisticaPartidoJugadorItem.SegundosJugadoss[0]
    statsmatchplayer.points = estadisticaPartidoJugadorItem.Puntoss[0]
    statsmatchplayer.point_goals_2 = estadisticaPartidoJugadorItem.ConvertidosDoss[0]
    statsmatchplayer.point_goals_2_attempted = estadisticaPartidoJugadorItem.IntentosDoss[0]
    statsmatchplayer.point_goals_3 = estadisticaPartidoJugadorItem.ConvertidosTress[0]
    statsmatchplayer.point_goals_3_attempted = estadisticaPartidoJugadorItem.IntentosTress[0]
    statsmatchplayer.point_goals_1 = estadisticaPartidoJugadorItem.ConvertidosUnos[0]
    statsmatchplayer.point_goals_1_attempted = estadisticaPartidoJugadorItem.IntentosUnos[0]
    statsmatchplayer.off_rebounds = estadisticaPartidoJugadorItem.RebotesOfs[0]
    statsmatchplayer.def_rebounds = estadisticaPartidoJugadorItem.RebotesDefs[0]
    statsmatchplayer.assists = estadisticaPartidoJugadorItem.Asistenciass[0]
    statsmatchplayer.turnovers = estadisticaPartidoJugadorItem.BalonesRecs[0]
    statsmatchplayer.steals = estadisticaPartidoJugadorItem.BalonesPers[0]
    statsmatchplayer.blocks_pro = estadisticaPartidoJugadorItem.TaponesFavs[0]
    statsmatchplayer.block_against = estadisticaPartidoJugadorItem.TaponesCons[0]
    statsmatchplayer.mate = estadisticaPartidoJugadorItem.Matess[0]
    statsmatchplayer.faults_made = estadisticaPartidoJugadorItem.FaltasComs[0]
    statsmatchplayer.faults_received = estadisticaPartidoJugadorItem.FaltasRecs[0]
    statsmatchplayer.feb_val = estadisticaPartidoJugadorItem.Valoracions[0]
    statsmatchplayer.bm_val = estadisticaPartidoJugadorItem.Valoracions[0]
    statsmatchplayer.starter_player = estadisticaPartidoJugadorItem.CincoInicials[0]
    return statsmatchplayer

    
    